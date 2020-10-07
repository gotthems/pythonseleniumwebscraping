const request = require('request');
const cheerio = require('cheerio');
const axios = require('axios');

axios.get('https://www.nonolive.com/barisg').then((res)=>{

const $ = cheerio.load(res.data);



});
