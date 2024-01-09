#!/usr/bin/node
let noarg = 0;

exports.logMe = function (item) {
  console.log(noarg + ': ' + item);
  noarg++;
};
