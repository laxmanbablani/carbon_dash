const fs = require('fs');
const path = require('path');
const rdt = require('react-docgen-typescript');

const CARBON_REACT_DIR = path.resolve(__dirname, '../_ref/carbon-design-system/packages/react/src/components');

async function testDocgen() {
  const buttonPath = path.join(CARBON_REACT_DIR, 'Button', 'Button.tsx');
  try {
    const docs = rdt.parse(buttonPath);
    console.log(JSON.stringify(docs, null, 2));
  } catch (err) {
    console.error("Error parsing Button:", err.message);
  }
}

testDocgen();