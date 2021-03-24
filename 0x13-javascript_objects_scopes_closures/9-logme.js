#!/usr/bin/node
// Prints the number of arguments already printed and the new argument value
module.exports.logMe = function (item) {
  console.log(`${module.exports.logMe.count}: ${item}`);
  module.exports.logMe.count++;
};

module.exports.logMe.count = 0;
