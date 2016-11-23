'use strict';
goog.provide('Blockly.Blocks.variables');
goog.require('Blockly.Blocks');



//

Blockly.Blocks['var'] = {
  init: function() {
    this.appendDummyInput()
        .appendField(new Blockly.FieldTextInput("name"), "VAR");
    this.setOutput(true);
    this.setColour(210);
    this.setTooltip('');
    this.setHelpUrl('http://www.example.com/');
  }
};

Blockly.Blocks['var_coma'] = {
  init: function() {
    this.appendValueInput("NAME")
        .appendField(new Blockly.FieldTextInput("name"), "VAR");
    this.setOutput(true);
    this.setColour(210);
    this.setTooltip('');
    this.setHelpUrl('http://www.example.com/');
  }
};

Blockly.Blocks['decvariables'] = {
  init: function() {
    this.appendValueInput("varName")
        .setCheck(null)
        .appendField("var");
    this.appendDummyInput()
        .appendField(":")
        .appendField(new Blockly.FieldDropdown([["int", "int"], ["float", "float"], ["string", "string"], ["bool", "bool"], ["char", "char"]]), "type");
    this.setPreviousStatement(true);
    this.setNextStatement(true);   
    this.setColour(210);
    this.setTooltip('');
    this.setHelpUrl('http://www.example.com/');
  }
};


Blockly.Blocks['decarreglos'] = {
  init: function() {
    this.appendDummyInput()
        .appendField("var")
        .appendField(new Blockly.FieldTextInput(""), "varNombre")
        .appendField(":")
        .appendField(new Blockly.FieldDropdown([["int", "int"], ["bool", "bool"], ["string", "string"], ["char", "char"], ["var", "OPTIONNAME"]]), "NAME")
        .appendField("[")
        .appendField(new Blockly.FieldTextInput(""), "tam")
        .appendField("]");
    this.setPreviousStatement(true);
    this.setNextStatement(true);
    this.setColour(210);
    this.setTooltip('');
    this.setHelpUrl('http://www.example.com/');
  }
};

Blockly.Blocks['assignment'] = {
  init: function() {
    this.appendValueInput("NAME")
        .setAlign(Blockly.ALIGN_RIGHT)
        .appendField(new Blockly.FieldTextInput("var"), "NAME")
        .appendField(" =");
    this.setPreviousStatement(true);
    this.setNextStatement(true);
    this.setColour(210);
    this.setTooltip('');
    this.setHelpUrl('http://www.example.com/');
  }
};

Blockly.Blocks['asigarr'] = {
  init: function() {
    this.appendValueInput("NAME")
        .appendField(new Blockly.FieldTextInput(""), "nomArr")
        .appendField("[")
        .appendField(new Blockly.FieldTextInput("default"), "tamArr")
        .appendField("] =");
    this.setPreviousStatement(true);
    this.setNextStatement(true);
    this.setColour(210);
    this.setTooltip('');
    this.setHelpUrl('http://www.example.com/');
  }
};

