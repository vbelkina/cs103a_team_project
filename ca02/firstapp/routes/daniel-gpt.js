const express = require('express');
const router = express.Router();
const User = require('../models/User')
const DanielGPT = require('../models/GPT')


isLoggedIn = (req,res,next) => {
    if (res.locals.loggedIn) {
      next()
    } else {
      res.redirect('/login')
    }
  }

// get the value associated to the key
router.get('/daniel-gpt', isLoggedIn, 	
    async (req,res,next) => {
        const show = req.query.show
        let items=[]
        items = await DanielGPT.find({userId:req.user._id}).sort({createdAt:1})
        let response = ""
        res.render('daniel-gpt', {items, response})
})

router.post('/daniel-gpt', isLoggedIn, async (req, res, next) => {
    try {
      const { Configuration, OpenAIApi } = require('openai');
      const configuration = new Configuration({
        apiKey: process.env.OPENAI_API_KEY,
      });
  
      const openai = new OpenAIApi(configuration);
      const response = await openai.createCompletion({
        model: 'text-davinci-003',
        prompt: "Translate the following text into Hebrew: \n" + req.body.vb_input,
        max_tokens: 1024,
        temperature: 0,
      });

      console.log(response)
  
      const daniel_gpt = new DanielGPT({
        entry: req.body.vb_input,
        reply: response.data.choices && response.data.choices.length > 0 ? response.data.choices[0].text : '', 
        language: 'Hebrew',
        createdAt: new Date(),
        userId: req.user._id,
      });
  
      await daniel_gpt.save();
  
      const items = await DanielGPT.find({ userId: req.user._id }).sort({ createdAt: 1 });

      res.render('daniel-gpt', { items, response });

    } catch (err) {
      console.error(err);
      next(err);
    }
  });

router.get('/daniel-gpt/remove/:itemId',
isLoggedIn,
async (req, res, next) => {
    console.log("inside /daniel-gpt/remove/:itemId")
    await DanielGPT.deleteOne({_id:req.params.itemId});
    res.redirect('/daniel-gpt')
});

module.exports = router;
