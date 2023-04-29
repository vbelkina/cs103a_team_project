
'use strict';
const mongoose = require( 'mongoose' );
const Schema = mongoose.Schema;
const ObjectId = mongoose.Schema.Types.ObjectId;

var VeronikaGPTSchema = Schema( {
  userId: {type:ObjectId, ref:'user' },
  entry: String, 
  reply: String,
  createdAt: Date
} );

module.exports = mongoose.model( 'VeronikaGPT', VeronikaGPTSchema );
