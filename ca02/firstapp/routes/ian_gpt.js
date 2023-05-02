const express = require('express');
const router = express.Router();
const User = require('../models/User')
const ianGPT = require('../models/GPT')


isLoggedIn = (req,res,next) => {
    if (res.locals.loggedIn) {
      next()
    } else {
      res.redirect('/login')
    }
  }

// get the value associated to the key
router.get('/ian_gpt', isLoggedIn, 
    async (req,res,next) => {
        const show = req.query.show
        let items=[]
        items = await ianGPT.find({userId:req.user._id}).sort({createdAt:1})
        let response = ""
        res.render('ian_gpt', {items, response})
})

router.post('/ian_gpt', isLoggedIn, async (req, res, next) => {
    try {
      const { Configuration, OpenAIApi } = require('openai');
      const configuration = new Configuration({
        apiKey: process.env.OPENAI_API_KEY,
      });
  
      const openai = new OpenAIApi(configuration);
      const response = await openai.createCompletion({
        model: 'text-davinci-003',
        prompt: "Render the following into French. Append to the translation a gloss and explanation of conjugations: \n" + req.body.input,
        max_tokens: 1024,
        temperature: 0,
      });

      console.log(response)
  
      const ian_gpt = new ianGPT({
        entry: req.body.input,
        reply: response.data.choices && response.data.choices.length > 0 ? response.data.choices[0].text : '', 
        language: 'French',
        createdAt: new Date(),
        userId: req.user._id,
      });
  
      await ian_gpt.save();
  
      const items = await ianGPT.find({ userId: req.user._id }).sort({ createdAt: 1 });

      res.render('ian_gpt', { items, response });

    } catch (err) {
      console.error(err);
      next(err);
    }
  });

router.get('/ian_gpt/remove/:itemId',
isLoggedIn,
async (req, res, next) => {
    console.log("inside /ian_gpt/remove/:itemId")
    await GPT.deleteOne({_id:req.params.itemId});
    res.redirect('/ian_gpt')
});

module.exports = router;