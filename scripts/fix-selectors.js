const fs = require('fs');
const path = require('path');
const CONFIG_PATH = 'scripts/config.json';
const config = JSON.parse(fs.readFileSync(CONFIG_PATH, 'utf8'));

const fixList = {
    "AILabel": ".cds--ai-label",
    "AISkeleton": ".cds--skeleton",
    "AspectRatio": ".cds--aspect-ratio",
    "BadgeIndicator": ".cds--badge-indicator",
    "ButtonSet": ".cds--btn-set",
    "ChatButton": ".cds--chat-btn",
    "CheckboxGroup": ".cds--checkbox-group",
    "CodeSnippet": ".cds--snippet",
    "ComboBox": ".cds--combo-box",
    "ComboButton": ".cds--combo-button",
    "ComposedModal": ".cds--modal",
    "ContainedList": ".cds--contained-list",
    "ContentSwitcher": ".cds--content-switcher",
    "ContextMenu": ".cds--context-menu",
    "Copy": ".cds--copy",
    "CopyButton": ".cds--copy-btn",
    "DangerButton": ".cds--btn--danger",
    "DataTable": ".cds--data-table",
    "DatePicker": ".cds--date-picker",
    "FileUploader": ".cds--file",
    "Link": ".cds--link",
    "ListBox": ".cds--list-box",
    "Notification": ".cds--inline-notification",
    "ProgressBar": ".cds--progress-bar",
    "Search": ".cds--search",
    "SkeletonText": ".cds--skeleton__text",
    "Tag": ".cds--tag"
};

for (const [name, selector] of Object.entries(fixList)) {
    if (config[name]) {
        config[name].testStrategy.selector = selector;
    }
}

fs.writeFileSync(CONFIG_PATH, JSON.stringify(config, null, 2));
console.log('Selectors updated.');
