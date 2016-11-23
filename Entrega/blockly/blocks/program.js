'use strict';

goog.provide('Blockly.Blocks.program');
goog.require('Blockly.Blocks');

Blockly.Blocks['program'] = {
  init: function() {
    this.appendDummyInput()
        .appendField("Program")
        .appendField(new Blockly.FieldTextInput("id"), "ID");
    this.setNextStatement(true);
    this.setColour(20);
    this.setTooltip('');
    this.setHelpUrl('http://www.example.com/');
  }
};

Blockly.Blocks['main'] = {
  init: function() {
    this.appendDummyInput()
        .appendField("main");
    this.appendStatementInput("NAME");
    this.setPreviousStatement(true);
    this.setColour(20);
    this.setTooltip('');
    this.setHelpUrl('http://www.example.com/');
  }
};
