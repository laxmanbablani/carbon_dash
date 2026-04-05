const fs = require('fs');
const path = require('path');
const config = require('./config.json');

const fixList = {
  "RadioButtonGroup": {
    "testStrategy": {
      "type": "click",
      "selector": "label[for='opt1']",
      "targetProp": "valueSelected",
      "expectedValue": "opt1"
    }
  },
  "RadioButton": {
     "testStrategy": {
        "type": "click",
        "selector": "label[for='test-radiobutton']",
        "targetProp": "checked",
        "expectedValue": true
     }
  },
  "Select": {
     "testStrategy": {
        "type": "click",
        "selector": "#test-select option[value='Option 1']",
        "targetProp": "value",
        "expectedValue": "Option 1"
     }
  },
  "Slider": {
     "testStrategy": {
        "type": "click",
        "selector": ".cds--slider__track",
        "targetProp": "value",
        "expectedValue": 50
     }
  }
};

for (const [name, data] of Object.entries(fixList)) {
  if (config[name]) {
    config[name].testStrategy = data.testStrategy;
  }
}

fs.writeFileSync(path.join(__dirname, 'config.json'), JSON.stringify(config, null, 2));
console.log('Updated test strategies in config.json');
