const express = require('express');
const router = express.Router();
const User = require('../models/User')
const KevinGPT = require('../models/GPT')


isLoggedIn = (req,res,next) => {
    if (res.locals.loggedIn) {
      next()
    } else {
      res.redirect('/login')
    }
  }

// get the value associated to the key
router.get('/kevin_gpt', isLoggedIn, 	
    async (req,res,next) => {
        const show = req.query.show
        let items=[]
        items = await KevinGPT.find({userId:req.user._id}).sort({createdAt:1})
        let response = ""
        res.render('kevin_gpt', {items, response})
})

router.post('/kevin_gpt', isLoggedIn, async (req, res, next) => {
    try {
      const { Configuration, OpenAIApi } = require('openai');
      const configuration = new Configuration({
        apiKey: process.env.OPENAI_API_KEY,
      });
  
      const openai = new OpenAIApi(configuration);
      const response = await openai.createCompletion({
        model: 'text-davinci-003',
        prompt: "Translate the following text into Mandarin: \n" + req.body.input,
        max_tokens: 1024,
        temperature: 0,
      });

      console.log(response)
  
      const kevin_gpt = new KevinGPT({
        entry: req.body.input,
        reply: response.data.choices && response.data.choices.length > 0 ? response.data.choices[0].text : '', 
        language: 'Mandarin',
        createdAt: new Date(),
        userId: req.user._id,
      });
  
      await kevin_gpt.save();
  
      const items = await KevinGPT.find({ userId: req.user._id }).sort({ createdAt: 1 });

      res.render('kevin_gpt', { items, response });

    } catch (err) {
      console.error(err);
      next(err);
    }
  });

router.get('/kevin_gpt/remove/:itemId',
isLoggedIn,
async (req, res, next) => {
    console.log("inside /kevin_gpt/remove/:itemId")
    await KevinGPT.deleteOne({_id:req.params.itemId});
    res.redirect('/kevin_gpt')
});

module.exports = router;