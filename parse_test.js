const parser = require('@babel/parser');
const traverse = require('@babel/traverse').default;

const code = `
export const Multiline = (args) => {
  return (
    <CodeSnippet type="multi" feedback="Copied to clipboard" {...args}>
      {\`Some code string\`}
    </CodeSnippet>
  );
};
`;

const ast = parser.parse(code, {
    sourceType: 'module',
    plugins: ['jsx', 'typescript']
});

traverse(ast, {
    JSXElement(path) {
        console.log(path.node.openingElement.name.name);
    }
});
