
'use strict';
const mongoose = require( 'mongoose' );
const Schema = mongoose.Schema;
const ObjectId = mongoose.Schema.Types.ObjectId;

var GPTSchema = Schema( {
  userId: {type:ObjectId, ref:'user' },
  entry: String, 
  reply: String,
  language: String,
  createdAt: Date
} );

module.exports = mongoose.model( 'GPT', GPTSchema );
