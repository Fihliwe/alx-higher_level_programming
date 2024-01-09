#!/usr/bin/node
// rectangle class
// constructor will be added with w and h and initialized


module.exports = class Rectangle {
  constructor (w, h) {
    this.width = w;
    this.height = h;

    if (w <= 0 || h <= 0 || !Number.isInteger(w) || !Number.isInteger(h)) {
    return {};
    }
  }
};
