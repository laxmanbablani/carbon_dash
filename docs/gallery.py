import carbon_dash
from dash import Dash, html, dcc, Input, Output

app = Dash(__name__)

# Component Stories
stories_dict = {}

stories_dict['node-ailabel'] = html.Div([
        html.H2("AILabel"),
        html.H3("Inline"),
        carbon_dash.AILabel(id='ailabel-inline'),
        html.H3("InlineWithContent"),
        carbon_dash.AILabel(id='ailabel-inlinewithcontent'),
    ])

stories_dict['node-accordion'] = html.Div([
        html.H2("Accordion"),
        html.H3("Controlled"),
        carbon_dash.Accordion(id='accordion-controlled'),
        html.H3("_WithLayer"),
        html.Div(children=carbon_dash.Accordion(children=[carbon_dash.AccordionItem(title='Choose your plan', children=html.Div(children='Compare plan features and select the option that best matches your\n            team\'s expected usage.')), carbon_dash.AccordionItem(title='Add team members', children=html.Div(children='Invite collaborators by email and assign their workspace roles\n            before launch.')), carbon_dash.AccordionItem(title='Set payment details', children=html.Div(children='Add billing information and choose whether to receive invoices by\n            email.')), carbon_dash.AccordionItem(title='Review and confirm', children=html.Div(children='Check your setup summary, then confirm to create the workspace for\n            your team.'))])),
        html.H3("Skeleton"),
        carbon_dash.AccordionSkeleton(open=True, count=4),
    ])

stories_dict['node-breadcrumb'] = html.Div([
        html.H2("Breadcrumb"),
        html.H3("BreadcrumbWithOverflowMenu"),
        carbon_dash.Breadcrumb(noTrailingSlash=True, children=[carbon_dash.BreadcrumbItem(children=html.Div(children='Breadcrumb 1')), carbon_dash.BreadcrumbItem(href='#', children='Breadcrumb 2'), carbon_dash.BreadcrumbItem(children=carbon_dash.OverflowMenu(align='bottom', children=[carbon_dash.OverflowMenuItem(itemText='Breadcrumb 3'), carbon_dash.OverflowMenuItem(itemText='Breadcrumb 4')])), carbon_dash.BreadcrumbItem(href='#', children='Breadcrumb 5'), carbon_dash.BreadcrumbItem(isCurrentPage=True, children='Breadcrumb 6')]),
        html.H3("BreadcrumbWithOverflowMenuSizeSmall"),
        carbon_dash.Breadcrumb(noTrailingSlash=True, children=[carbon_dash.BreadcrumbItem(children=html.Div(children='Breadcrumb 1')), carbon_dash.BreadcrumbItem(href='#', children='Breadcrumb 2'), carbon_dash.BreadcrumbItem(children=carbon_dash.OverflowMenu(align='bottom', children=[carbon_dash.OverflowMenuItem(itemText='Breadcrumb 3'), carbon_dash.OverflowMenuItem(itemText='Breadcrumb 4')])), carbon_dash.BreadcrumbItem(href='#', children='Breadcrumb 5'), carbon_dash.BreadcrumbItem(isCurrentPage=True, children='Breadcrumb 6')]),
        html.H3("Skeleton"),
        carbon_dash.BreadcrumbSkeleton(),
        html.H3("BreadcrumbWithOverflowVisualSnapshots"),
        carbon_dash.Breadcrumb(noTrailingSlash=True, children=[carbon_dash.BreadcrumbItem(children=html.Div(children='Breadcrumb 1')), carbon_dash.BreadcrumbItem(href='#', children='Breadcrumb 2'), carbon_dash.BreadcrumbItem(children=carbon_dash.OverflowMenu(align='bottom', children=[carbon_dash.OverflowMenuItem(itemText='Breadcrumb 3'), carbon_dash.OverflowMenuItem(itemText='Breadcrumb 4')])), carbon_dash.BreadcrumbItem(href='#', children='Breadcrumb 5'), carbon_dash.BreadcrumbItem(isCurrentPage=True, children='Breadcrumb 6')]),
    ])

stories_dict['node-button'] = html.Div([
        html.H2("Button"),
        html.H3("Secondary"),
        carbon_dash.Button(children='Button'),
        html.H3("Tertiary"),
        carbon_dash.Button(children='Button'),
        html.H3("Ghost"),
        carbon_dash.Button(children='Button'),
        html.H3("Danger"),
        carbon_dash.Button(children='Button'),
        html.H3("DangerTertiary"),
        carbon_dash.Button(children='Button'),
        html.H3("DangerGhost"),
        carbon_dash.Button(children='Button'),
        html.H3("IconButton"),
        carbon_dash.Button(),
        html.H3("IconButtonWithBadge"),
        carbon_dash.Button(children='Button'),
        html.H3("Skeleton"),
        carbon_dash.ButtonSkeleton(),
    ])

stories_dict['node-buttonset'] = html.Div([
        html.H2("ButtonSet"),
        html.H3("Fluid"),
        carbon_dash.ButtonSet(id='buttonset-fluid'),
    ])

stories_dict['node-checkbox'] = html.Div([
        html.H2("Checkbox"),
        html.H3("Horizontal"),
        carbon_dash.CheckboxGroup(orientation='horizontal', className='some-class', legendText='Group label', helperText='Helper text goes here', children=[carbon_dash.Checkbox(id='checkbox-label-1'), carbon_dash.Checkbox(id='checkbox-label-2'), carbon_dash.Checkbox(id='checkbox-label-3')]),
        html.H3("Single"),
        carbon_dash.Checkbox(id='checkbox-single'),
        html.H3("Skeleton"),
        carbon_dash.CheckboxSkeleton(),
        html.H3("withAILabel"),
        html.Div(className='ai-label-check-radio-container', children=[carbon_dash.CheckboxGroup(legendText='Group Label', children=[carbon_dash.Checkbox(id='checkbox-label-1'), carbon_dash.Checkbox(id='checkbox-label-2'), carbon_dash.Checkbox(id='checkbox-label-3')]), carbon_dash.CheckboxGroup(legendText='Group Label', children=[carbon_dash.Checkbox(id='checkbox-label-4'), carbon_dash.Checkbox(id='checkbox-label-5'), carbon_dash.Checkbox(id='checkbox-label-6')]), carbon_dash.CheckboxGroup(legendText='Group Label', children=[carbon_dash.Checkbox(id='checkbox-label-7'), carbon_dash.Checkbox(id='checkbox-label-8'), carbon_dash.Checkbox(id='checkbox-label-9')])]),
    ])

stories_dict['node-codesnippet'] = html.Div([
        html.H2("CodeSnippet"),
        html.H3("Inline"),
        carbon_dash.CodeSnippet(type='inline', feedback='Copied to clipboard', children='node -v'),
        html.H3("Multiline"),
        carbon_dash.CodeSnippet(type='multi', feedback='Copied to clipboard', children='"scripts": {\n    "build": "lerna run build --stream --prefix --npm-client yarn",\n    "ci-check": "carbon-cli ci-check",\n    "clean": "lerna run clean && lerna clean --yes && rimraf node_modules",\n    "doctoc": "doctoc --title \'## Table of Contents\'",\n    "format": "prettier --write \'**/*.{js,md,scss,ts}\' \'!**/{build,es,lib,storybook,ts,umd}/**\'",\n    "format:diff": "\n    prettier --list-different \'**/*.{js,md,scss,ts}\' \'!**/{build,es,lib,storybook,ts,umd}/**\' \'!packages/components/**\'",\n    "lint": "eslint actions config codemods packages",\n    "lint:styles": "stylelint \'**/*.{css,scss}\' --report-needless-disables --report-invalid-scope-disables",\n    "test": "cross-env BABEL_ENV=test jest",\n    "test:e2e": "cross-env BABEL_ENV=test jest --testPathPattern=e2e --testPathIgnorePatterns=\'examples,/packages/components/,/packages/react/\'"\n  },\n  "resolutions": {\n    "react": "~16.9.0",\n    "react-dom": "~16.9.0",\n    "react-is": "~16.9.0",\n    "react-test-renderer": "~16.9.0"\n  },\n  "devDependencies": {\n    "@babel/core": "^7.10.0",\n    "@babel/plugin-proposal-class-properties": "^7.7.4",\n    "@babel/plugin-proposal-export-default-from": "^7.7.4",\n    "@babel/plugin-proposal-export-namespace-from": "^7.7.4",\n    "@babel/plugin-transform-runtime": "^7.10.0",\n    "@babel/preset-env": "^7.10.0",\n    "@babel/preset-react": "^7.10.0",\n    "@babel/runtime": "^7.10.0",\n    "@commitlint/cli": "^8.3.5",'),
        html.H3("Singleline"),
        carbon_dash.CodeSnippet(type='single', feedback='Copied to clipboard', children='yarn add carbon-components@latest carbon-components-react@latest\n      @carbon/icons-react@latest carbon-icons@latest'),
        html.H3("InlineWithLayer"),
        html.Div(children=carbon_dash.CodeSnippet(type='inline', feedback='Copied to clipboard', children='node -v')),
        html.H3("MultilineWithLayer"),
        html.Div(children=carbon_dash.CodeSnippet(type='multi', feedback='Copied to clipboard', children='"scripts": {\n      "build": "lerna run build --stream --prefix --npm-client yarn",\n      "ci-check": "carbon-cli ci-check",\n      "clean": "lerna run clean && lerna clean --yes && rimraf node_modules",\n      "doctoc": "doctoc --title \'## Table of Contents\'",\n      "format": "prettier --write \'**/*.{js,md,scss,ts}\' \'!**/{build,es,lib,storybook,ts,umd}/**\'",\n      "format:diff": "prettier --list-different \'**/*.{js,md,scss,ts}\' \'!**/{build,es,lib,storybook,ts,umd}/**\' \'!packages/components/**\'",\n      "lint": "eslint actions config codemods packages",\n      "lint:styles": "stylelint \'**/*.{css,scss}\' --report-needless-disables --report-invalid-scope-disables",\n      "test": "cross-env BABEL_ENV=test jest",\n      "test:e2e": "cross-env BABEL_ENV=test jest --testPathPattern=e2e --testPathIgnorePatterns=\'examples,/packages/components/,/packages/react/\'"\n      },\n      "resolutions": {\n        "react": "~16.9.0",\n        "react-dom": "~16.9.0",\n        "react-is": "~16.9.0",\n        "react-test-renderer": "~16.9.0"\n      },\n      "devDependencies": {\n        "@babel/core": "^7.10.0",\n        "@babel/plugin-proposal-class-properties": "^7.7.4",\n        "@babel/plugin-proposal-export-default-from": "^7.7.4",\n        "@babel/plugin-proposal-export-namespace-from": "^7.7.4",\n        "@babel/plugin-transform-runtime": "^7.10.0",\n        "@babel/preset-env": "^7.10.0",\n        "@babel/preset-react": "^7.10.0",\n        "@babel/runtime": "^7.10.0",\n        "@commitlint/cli": "^8.3.5",')),
        html.H3("SinglelineWithLayer"),
        html.Div(children=carbon_dash.CodeSnippet(type='single', feedback='Copied to clipboard', children='yarn add carbon-components@latest carbon-components-react@latest\n        @carbon/icons-react@latest carbon-icons@latest')),
        html.H3("Skeleton"),
        html.Div(children=[carbon_dash.CodeSnippetSkeleton(type='single'), carbon_dash.CodeSnippetSkeleton(type='multi')]),
    ])

stories_dict['node-combobox'] = html.Div([
        html.H2("ComboBox"),
        html.H3("FloatingStyles"),
        html.Div(children=carbon_dash.ComboBox(id='carbon-combobox', titleText='Label', helperText='Helper text', invalidText='Error message goes here', warnText='Warning message goes here')),
        html.H3("AllowCustomValue"),
        html.Div(children=carbon_dash.ComboBox(allowCustomValue=True, id='carbon-combobox', titleText='Label', helperText='Helper text', invalidText='Error message goes here', warnText='Warning message goes here')),
        html.H3("AutocompleteWithTypeahead"),
        html.Div(children=carbon_dash.ComboBox(helperText='Helper text', invalidText='Error message goes here', warnText='Warning message goes here', id='carbon-combobox', titleText='Label', typeahead=True)),
        html.H3("ExperimentalAutoAlign"),
        html.Div(children=[html.Div(), carbon_dash.ComboBox(id='carbon-combobox', titleText='Label', helperText='Helper text', autoAlign=True), html.Div()]),
        html.H3("_WithLayer"),
        html.Div(),
        html.H3("withAILabel"),
        html.Div(children=carbon_dash.ComboBox(id='carbon-combobox', titleText='Label', helperText='Helper text')),
        html.H3("Controlled"),
        html.Div(children=[carbon_dash.ComboBox(id='carbon-combobox', titleText='Label', helperText='Helper text'), html.Div(children=[carbon_dash.Button(children='Clear'), carbon_dash.Button(children='Option 1'), carbon_dash.Button(children='Option 2'), carbon_dash.Button(children='Option 3')])]),
    ])

stories_dict['node-combobutton'] = html.Div([
        html.H2("ComboButton"),
        html.H3("FloatingStyles"),
        carbon_dash.ComboButton(label='Primary action', children=[carbon_dash.MenuItem(label='Second action with a long label description'), carbon_dash.MenuItem(label='Third action'), carbon_dash.MenuItem(label='Fourth action', disabled=True)]),
        html.H3("ExperimentalAutoAlign"),
        html.Div(children=[html.Div(children=carbon_dash.ComboButton(label='Primary action', children=[carbon_dash.MenuItem(label='Second action with a long label description'), carbon_dash.MenuItem(label='Third action'), carbon_dash.MenuItem(label='Fourth action', disabled=True)])), ' ']),
        html.H3("WithDanger"),
        carbon_dash.ComboButton(label='Primary action', children=[carbon_dash.MenuItem(label='Second action with a long label description'), carbon_dash.MenuItem(label='Third action'), carbon_dash.MenuItem(label='Fourth action'), carbon_dash.MenuItemDivider(), carbon_dash.MenuItem(label='Danger action', kind='danger')]),
        html.H3("WithIcons"),
        carbon_dash.ComboButton(label='Save record', children=[carbon_dash.MenuItem(label='Save as a copy'), carbon_dash.MenuItem(label='Export')]),
        html.H3("WithMenuAlignment"),
        carbon_dash.ComboButton(id='combobutton-withmenualignment'),
    ])

stories_dict['node-composedmodal'] = html.Div([
        html.H2("ComposedModal"),
        html.H3("EnableDialogElement"),
        carbon_dash.FeatureFlags(enableDialogElement=True, children=html.Div(children=[carbon_dash.Button(children='Launch composed modal'), carbon_dash.ComposedModal(children=[carbon_dash.ModalHeader(label='Account resources', title='Add a custom domain'), carbon_dash.ModalBody(children=[html.Div(children='Custom domains direct requests for your apps in this Cloud Foundry\n              organization to a URL that you own. A custom domain can be a\n              shared domain, a shared subdomain, or a shared domain and host.'), carbon_dash.TextInput(id='text-input-1', labelText='Domain name', placeholder='e.g. github.com'), carbon_dash.Select(id='select-1', defaultValue='us-south', labelText='Region', children=[carbon_dash.SelectItem(value='us-south', text='US South'), carbon_dash.SelectItem(value='us-east', text='US East')])]), carbon_dash.ModalFooter(primaryButtonText='Add', secondaryButtonText='Cancel')])])),
        html.H3("EnableFocusWrapWithoutSentinels"),
        carbon_dash.FeatureFlags(enableFocusWrapWithoutSentinels=True, children=html.Div(children=[carbon_dash.Button(children='Launch composed modal'), carbon_dash.ComposedModal(children=[carbon_dash.ModalHeader(label='Account resources', title='Add a custom domain'), carbon_dash.ModalBody(children=[html.Div(children='Custom domains direct requests for your apps in this Cloud Foundry\n              organization to a URL that you own. A custom domain can be a\n              shared domain, a shared subdomain, or a shared domain and host.'), carbon_dash.TextInput(id='text-input-1', labelText='Domain name', placeholder='e.g. github.com'), carbon_dash.Select(id='select-1', defaultValue='us-south', labelText='Region', children=[carbon_dash.SelectItem(value='us-south', text='US South'), carbon_dash.SelectItem(value='us-east', text='US East')])]), carbon_dash.ModalFooter(primaryButtonText='Add', secondaryButtonText='Cancel')])])),
        html.H3("FullWidth"),
        carbon_dash.ComposedModal(id='composedmodal-fullwidth'),
        html.H3("PassiveModal"),
        carbon_dash.ComposedModal(id='composedmodal-passivemodal'),
        html.H3("WithStateManager"),
        html.Div(),
        html.H3("WithScrollingContent"),
        carbon_dash.ComposedModal(id='composedmodal-withscrollingcontent'),
        html.H3("WithInlineLoading"),
        carbon_dash.ComposedModal(id='composedmodal-withinlineloading'),
        html.H3("_withAILabel"),
        carbon_dash.ComposedModal(id='composedmodal-_withailabel'),
        html.H3("EnablePresence"),
        carbon_dash.FeatureFlags(enablePresence=True, children=html.Div(children=[carbon_dash.Button(children='Launch composed modal'), carbon_dash.ClassPrefix(prefix='presence', children=html.Div(className='preview-modal-with-presence', children=carbon_dash.ComposedModal(children=[carbon_dash.ModalHeader(label='Account resources', title='Add a custom domain'), carbon_dash.ModalBody(children=[html.Div(children='Custom domains direct requests for your apps in this Cloud\n                  Foundry organization to a URL that you own. A custom domain\n                  can be a shared domain, a shared subdomain, or a shared domain\n                  and host.'), carbon_dash.TextInput(id='text-input-1', labelText='Domain name', placeholder='e.g. github.com'), carbon_dash.Select(id='select-1', defaultValue='us-south', labelText='Region', children=[carbon_dash.SelectItem(value='us-south', text='US South'), carbon_dash.SelectItem(value='us-east', text='US East')])]), carbon_dash.ModalFooter(primaryButtonText='Add', secondaryButtonText='Cancel')])))])),
    ])

stories_dict['node-containedlist'] = html.Div([
        html.H2("ContainedList"),
        html.H3("Disclosed"),
        carbon_dash.ContainedList(id='containedlist-disclosed'),
        html.H3("WithInteractiveItems"),
        carbon_dash.ContainedList(label='List title', kind='on-page', children=[carbon_dash.ContainedListItem(children='List item'), carbon_dash.ContainedListItem(disabled=True, children='List item'), carbon_dash.ContainedListItem(children='List item'), carbon_dash.ContainedListItem(children='List item')]),
        html.H3("WithActions"),
        carbon_dash.ContainedList(label='List title', kind='on-page', action='', children=[carbon_dash.ContainedListItem(children='List item'), carbon_dash.ContainedListItem(disabled=True, children='List item'), carbon_dash.ContainedListItem(children='List item'), carbon_dash.ContainedListItem(children='List item')]),
        html.H3("WithExpandableSearch"),
        carbon_dash.ContainedList(label='List title', kind='on-page'),
        html.H3("WithPersistentSearch"),
        carbon_dash.ContainedList(label='List title', kind='on-page', action='', children=carbon_dash.Search(placeholder='Filter', closeButtonLabelText='Clear search input', size='lg', labelText='Filter search')),
        html.H3("WithInteractiveItemsAndActions"),
        carbon_dash.ContainedList(label='List title', kind='on-page', action='', children=[carbon_dash.ContainedListItem(children='List item'), carbon_dash.ContainedListItem(children='List item'), carbon_dash.ContainedListItem(children='List item'), carbon_dash.ContainedListItem(children='List item')]),
        html.H3("WithListTitleDecorators"),
        carbon_dash.ContainedList(kind='on-page', children=[carbon_dash.ContainedListItem(children='List item'), carbon_dash.ContainedListItem(children='List item'), carbon_dash.ContainedListItem(children='List item'), carbon_dash.ContainedListItem(children='List item')]),
        html.H3("WithIcons"),
        carbon_dash.ContainedList(label='List title', kind='on-page', children=[carbon_dash.ContainedListItem(children='List item'), carbon_dash.ContainedListItem(children='List item'), carbon_dash.ContainedListItem(children='List item'), carbon_dash.ContainedListItem(children='List item')]),
        html.H3("_WithLayer"),
        html.Div(children=carbon_dash.ContainedList(label='List title', kind='on-page', children=[carbon_dash.ContainedListItem(children='List item'), carbon_dash.ContainedListItem(children='List item')])),
        html.H3("UsageExamples"),
        carbon_dash.ContainedList(id='containedlist-usageexamples'),
    ])

stories_dict['node-contentswitcher'] = html.Div([
        html.H2("ContentSwitcher"),
        html.H3("_WithLayer"),
        html.Div(children=carbon_dash.ContentSwitcher(children=[carbon_dash.Switch(name='one', text='First section'), carbon_dash.Switch(name='two', text='Second section'), carbon_dash.Switch(name='three', text='Third section')])),
        html.H3("IconOnly"),
        carbon_dash.ContentSwitcher(children=[carbon_dash.IconSwitch(name='one', text='Table of Contents', children=html.Div()), carbon_dash.IconSwitch(name='two', text='Workspace Test', children=html.Div()), carbon_dash.IconSwitch(name='three', text='View Mode', children=html.Div())]),
        html.H3("IconOnlyWithLayer"),
        html.Div(children=carbon_dash.ContentSwitcher(children=[carbon_dash.IconSwitch(name='one', text='Table of Contents', children=html.Div()), carbon_dash.IconSwitch(name='two', text='Workspace Test', children=html.Div()), carbon_dash.IconSwitch(name='three', text='View Mode', children=html.Div())])),
        html.H3("lowContrast"),
        carbon_dash.ContentSwitcher(lowContrast=True, children=[carbon_dash.Switch(name='one', text='First section'), carbon_dash.Switch(name='two', text='Second section'), carbon_dash.Switch(name='three', text='Third section')]),
        html.H3("lowContrastIconOnly"),
        carbon_dash.ContentSwitcher(lowContrast=True, children=[carbon_dash.IconSwitch(name='one', text='Table of Contents', children=html.Div()), carbon_dash.IconSwitch(name='two', text='Workspace Test', children=html.Div()), carbon_dash.IconSwitch(name='three', text='View Mode', children=html.Div())]),
    ])

stories_dict['node-datatable'] = html.Div([
        html.H2("DataTable"),
        html.H3("AILabelWithSelection"),
        carbon_dash.DataTable(),
        html.H3("AILabelWithRadioSelection"),
        carbon_dash.DataTable(radio=True),
        html.H3("AILabelWithSelectionAndExpansion"),
        carbon_dash.DataTable(),
        html.H3("AILabelWithExpansion"),
        carbon_dash.DataTable(),
        html.H3("ColumnAILabelWithSelectionAndExpansion"),
        carbon_dash.DataTable(),
        html.H3("ColumnAILabelSort"),
        carbon_dash.DataTable(),
        html.H3("FullTableAI"),
        carbon_dash.DataTable(),
        html.H3("XLWithTwoLines"),
        carbon_dash.Table(children=[carbon_dash.TableHead(children=carbon_dash.TableRow()), carbon_dash.TableBody()]),
        html.H3("WithRadioSelection"),
        carbon_dash.DataTable(radio=True),
        html.H3("WithSelectionAndSorting"),
        carbon_dash.DataTable(isSortable=True),
        html.H3("PersistentToolbar"),
        carbon_dash.DataTable(),
        html.H3("SmallPersistentToolbar"),
        carbon_dash.DataTable(),
        html.H3("WithOverflowMenu"),
        carbon_dash.DataTable(),
        html.H3("BatchExpansion"),
        carbon_dash.DataTable(),
        html.H3("BatchExpansionMultipleTables"),
        carbon_dash.DataTable(id='datatable-batchexpansionmultipletables'),
    ])

stories_dict['node-datatableskeleton'] = html.Div([
        html.H2("DataTableSkeleton"),
        html.H3("Skeleton"),
        html.Div(children=[carbon_dash.DataTableSkeleton(), html.Div()]),
    ])

stories_dict['node-datepicker'] = html.Div([
        html.H2("DatePicker"),
        html.H3("Simple"),
        carbon_dash.DatePicker(datePickerType='simple', children=carbon_dash.DatePickerInput(placeholder='mm/dd/yyyy', labelText='Date Picker label', id='date-picker-simple')),
        html.H3("SingleWithCalendar"),
        carbon_dash.DatePicker(datePickerType='single', children=carbon_dash.DatePickerInput(placeholder='mm/dd/yyyy', labelText='Date Picker label', id='date-picker-single', size='md')),
        html.H3("RangeWithCalendar"),
        carbon_dash.DatePicker(datePickerType='range', children=[carbon_dash.DatePickerInput(id='date-picker-input-id-start', placeholder='mm/dd/yyyy', labelText='Start date', size='md'), carbon_dash.DatePickerInput(id='date-picker-input-id-finish', placeholder='mm/dd/yyyy', labelText='End date', size='md')]),
        html.H3("SimpleWithLayer"),
        html.Div(),
        html.H3("SingleWithCalendarWithLayer"),
        html.Div(),
        html.H3("RangeWithCalendarWithLayer"),
        html.Div(),
        html.H3("Skeleton"),
        carbon_dash.DatePickerSkeleton(range=True),
        html.H3("withAILabel"),
        html.Div(children=carbon_dash.DatePicker(datePickerType='single', children=carbon_dash.DatePickerInput(placeholder='mm/dd/yyyy', labelText='Date Picker label', size='md', id='date-picker'))),
    ])

stories_dict['node-dropdown'] = html.Div([
        html.H2("Dropdown"),
        html.H3("FloatingStyles"),
        html.Div(children=carbon_dash.Dropdown(id='default', titleText='Label', helperText='Helper text', label='Option 1')),
        html.H3("ExperimentalAutoAlign"),
        html.Div(children=[html.Div(), carbon_dash.Dropdown(autoAlign=True, id='default', titleText='Label', helperText='Helper text', label='Option 1', direction='top'), html.Div()]),
        html.H3("Inline"),
        html.Div(children=carbon_dash.Dropdown(id='inline', titleText='Label', label='Option 1', type='inline')),
        html.H3("_WithLayer"),
        html.Div(),
        html.H3("InlineWithLayer"),
        html.Div(),
        html.H3("Skeleton"),
        html.Div(children=carbon_dash.DropdownSkeleton()),
        html.H3("withAILabel"),
        html.Div(children=carbon_dash.Dropdown(id='default', titleText='Label', helperText='Helper text', label='Option 1')),
        html.H3("withToggletipLabel"),
        html.Div(children=carbon_dash.Dropdown(label='placeholder', id='dropdown')),
        html.H3("TestInvalidTextNoOverlap"),
        html.Div(children=[carbon_dash.Dropdown(id='test-1', titleText='Label', helperText='Helper text', label='Choose an option', invalid=True, invalidText='Error message goes here'), carbon_dash.Dropdown(titleText='Label', label='Choose an option', id='test-2')]),
    ])

stories_dict['node-errorboundary'] = html.Div([
        html.H2("ErrorBoundary"),
        html.H3("WithCustomContext"),
        html.Div(),
    ])

stories_dict['node-fileuploader'] = html.Div([
        html.H2("FileUploader"),
        html.H3("EnhancedCallbacks"),
        html.Div(children=carbon_dash.FileUploader(labelTitle='Enhanced FileUploader Demo', labelDescription='Open browser console to see detailed callback data when adding/removing files', buttonLabel='Add file(s)', buttonKind='primary', filenameStatus='edit', multiple=True, iconDescription='Remove uploaded file')),
        html.H3("_FileUploaderItem"),
        carbon_dash.FileUploaderItem(errorBody='1 MB max file size. Select a new file and try again.', errorSubject='File size exceeds limit', iconDescription='Delete file', invalid=False, name='THIS IS A VERY LONG FILENAME WHICH WILL BE TRUNCATED', status='edit', size='md'),
        html.H3("_FileUploaderDropContainer"),
        carbon_dash.FileUploaderDropContainer(labelText='Drag and drop files here or click to upload', multiple=True, disabled=False, name=''),
        html.H3("DragAndDropUploadContainerExampleApplication"),
        carbon_dash.FileUploader(id='fileuploader-draganddropuploadcontainerexampleapplication'),
        html.H3("DragAndDropUploadSingleContainerExampleApplication"),
        carbon_dash.FileUploader(id='fileuploader-draganddropuploadsinglecontainerexampleapplication'),
        html.H3("Skeleton"),
        html.Div(children=carbon_dash.FileUploaderSkeleton()),
    ])

stories_dict['node-fluidcombobox'] = html.Div([
        html.H2("FluidComboBox"),
        html.H3("Condensed"),
        html.Div(children=carbon_dash.FluidComboBox(id='default', isCondensed=True, titleText='Label', label='Choose an option')),
        html.H3("withAILabel"),
        html.Div(children=carbon_dash.FluidComboBox(id='default', titleText='Label', label='Choose an option')),
        html.H3("Skeleton"),
        html.Div(children=carbon_dash.FluidComboBoxSkeleton()),
    ])

stories_dict['node-fluiddatepicker'] = html.Div([
        html.H2("FluidDatePicker"),
        html.H3("Simple"),
        html.Div(children=carbon_dash.FluidDatePicker(children=carbon_dash.FluidDatePickerInput(placeholder='mm/dd/yyyy', id='date-picker-simple'))),
        html.H3("Single"),
        html.Div(children=carbon_dash.FluidDatePicker(children=carbon_dash.FluidDatePickerInput(placeholder='mm/dd/yyyy', id='date-picker-single'))),
        html.H3("RangeWithCalendar"),
        html.Div(children=carbon_dash.FluidDatePicker(children=[carbon_dash.FluidDatePickerInput(id='date-picker-input-id-start', placeholder='mm/dd/yyyy', size='md'), carbon_dash.FluidDatePickerInput(id='date-picker-input-id-finish', placeholder='mm/dd/yyyy', labelText='End date', size='md')])),
        html.H3("Skeleton"),
        html.Div(children=[carbon_dash.FluidDatePickerSkeleton(datePickerType='simple', id='input-1'), html.Div(), html.Div(), carbon_dash.FluidDatePickerSkeleton(datePickerType='single', id='input-2'), html.Div(), html.Div(), carbon_dash.FluidDatePickerSkeleton(datePickerType='range', id='input-3')]),
    ])

stories_dict['node-fluiddropdown'] = html.Div([
        html.H2("FluidDropdown"),
        html.H3("Condensed"),
        html.Div(children=carbon_dash.FluidDropdown(id='default', isCondensed=True, titleText='Label', label='Choose an option')),
        html.H3("withAILabel"),
        html.Div(children=carbon_dash.FluidDropdown(id='default', titleText='Label', label='Choose an option')),
        html.H3("Skeleton"),
        html.Div(children=carbon_dash.FluidDropdownSkeleton()),
    ])

stories_dict['node-fluidmultiselect'] = html.Div([
        html.H2("FluidMultiSelect"),
        html.H3("Filterable"),
        html.Div(children=carbon_dash.FluidMultiSelect(isFilterable=True, id='default', titleText='Label', label='Choose an option')),
        html.H3("_FilterableWithLayer"),
        html.Div(),
        html.H3("Condensed"),
        html.Div(children=carbon_dash.FluidMultiSelect(id='default', isCondensed=True, titleText='Label', label='Choose an option')),
        html.H3("withAILabel"),
        html.Div(children=carbon_dash.FluidMultiSelect(id='default', titleText='Label', label='Choose an option')),
        html.H3("Skeleton"),
        html.Div(children=carbon_dash.FluidMultiSelectSkeleton()),
    ])

stories_dict['node-fluidnumberinput'] = html.Div([
        html.H2("FluidNumberInput"),
        html.H3("Skeleton"),
        html.Div(children=carbon_dash.FluidNumberInputSkeleton(id='input-skeleton')),
    ])

stories_dict['node-fluidsearch'] = html.Div([
        html.H2("FluidSearch"),
        html.H3("Skeleton"),
        html.Div(children=carbon_dash.FluidSearchSkeleton()),
    ])

stories_dict['node-fluidselect'] = html.Div([
        html.H2("FluidSelect"),
        html.H3("withAILabel"),
        html.Div(children=carbon_dash.FluidSelect(id='select-1', labelText='Select an option', children=[carbon_dash.SelectItem(value='', text=''), carbon_dash.SelectItem(value='An example option that is really long to show what should be done to handle long text', text='An example option that is really long to show what should be done to handle long text'), carbon_dash.SelectItem(value='Option 2', text='Option 2'), carbon_dash.SelectItem(value='Option 3', text='Option 3'), carbon_dash.SelectItem(value='Option 4', text='Option 4')])),
        html.H3("Skeleton"),
        html.Div(children=carbon_dash.FluidSelectSkeleton()),
    ])

stories_dict['node-fluidtextarea'] = html.Div([
        html.H2("FluidTextArea"),
        html.H3("DefaultWithLayers"),
        html.Div(),
        html.H3("DefaultWithToggletip"),
        carbon_dash.FluidTextArea(placeholder='Placeholder text'),
        html.H3("Skeleton"),
        html.Div(children=carbon_dash.FluidTextAreaSkeleton()),
    ])

stories_dict['node-fluidtextinput'] = html.Div([
        html.H2("FluidTextInput"),
        html.H3("DefaultWithToggletip"),
        carbon_dash.FluidTextInput(placeholder='Placeholder text'),
        html.H3("Skeleton"),
        html.Div(children=carbon_dash.FluidTextInputSkeleton(id='input-1')),
    ])

stories_dict['node-fluidtimepicker'] = html.Div([
        html.H2("FluidTimePicker"),
        html.H3("Skeleton"),
        html.Div(children=[carbon_dash.FluidTimePickerSkeleton(), html.Div(), html.Div(), carbon_dash.FluidTimePickerSkeleton(isOnlyTwo=True)]),
    ])

stories_dict['node-form'] = html.Div([
        html.H2("Form"),
        html.H3("withAILabel"),
        carbon_dash.Stack(gap=7, className='form-example', children=[carbon_dash.Form(className='ai-label-form', children=carbon_dash.Stack(gap=7, children=[carbon_dash.NumberInput(), carbon_dash.DatePicker(datePickerType='single', children=carbon_dash.DatePickerInput(placeholder='mm/dd/yyyy', labelText='Date Picker label', size='md', id='date-picker')), carbon_dash.TextInput(), carbon_dash.TextArea(), carbon_dash.Dropdown(id='default', titleText='Dropdown title', helperText='This is some helper text', label='Option 1'), carbon_dash.MultiSelect(label='Multiselect Label', id='carbon-multiselect-example', titleText='Multiselect title', helperText='This is helper text', selectionFeedback='top-after-reopen'), carbon_dash.FilterableMultiSelect(id='carbon-multiselect-example-3', titleText='FilterableMultiselect title', selectionFeedback='top-after-reopen'), carbon_dash.ComboBox(id='carbon-combobox', titleText='ComboBox title', helperText='Combobox helper text'), carbon_dash.Select(id='select-1', labelText='Select an option', helperText='Optional helper text', children=[carbon_dash.SelectItem(value='', text=''), carbon_dash.SelectItem(value='An example option that is really long to show what should be done to handle long text', text='An example option that is really long to show what should be done to handle long text'), carbon_dash.SelectItem(value='Option 2', text='Option 2'), carbon_dash.SelectItem(value='Option 3', text='Option 3'), carbon_dash.SelectItem(value='Option 4', text='Option 4')]), carbon_dash.Button(type='submit', className='some-class', children='Submit')])), carbon_dash.FluidForm(className='fluid-ai-label-form', children=[html.Div(children=carbon_dash.FluidDatePicker(children=carbon_dash.FluidDatePickerInput(placeholder='mm/dd/yyyy', labelText='Date Picker label', size='md', id='fluid-date-picker'))), html.Div(children=carbon_dash.FluidNumberInput(id='fluid-number-input')), html.Div(children=carbon_dash.FluidTextInput(id='fluid-text-input')), html.Div(children=carbon_dash.FluidTextArea(id='fluid-text-area')), html.Div(children=carbon_dash.FluidDropdown(isCondensed=True, id='fluid-dropdown', titleText='Label', label='Choose an option')), html.Div(children=carbon_dash.FluidComboBox(isCondensed=True, id='fluid-combobox', titleText='Label', label='Choose an option')), html.Div(children=carbon_dash.FluidMultiSelect(isCondensed=True, id='fluid-multi-select', titleText='Label', label='Choose an option')), html.Div(children=carbon_dash.FluidMultiSelect(isFilterable=True, isCondensed=True, id='fluid-multi-select-2', titleText='Label', label='Choose an option')), html.Div(children=carbon_dash.FluidSelect(id='select-2', children=[carbon_dash.SelectItem(value='', text=''), carbon_dash.SelectItem(value='option-1', text='Option 1'), carbon_dash.SelectItem(value='option-2', text='Option 2'), carbon_dash.SelectItem(value='option-3', text='Option 3'), carbon_dash.SelectItem(value='option-4', text='Option 4')])), carbon_dash.Button(type='submit', className='some-class', children='Submit')])]),
    ])

stories_dict['node-formlabel'] = html.Div([
        html.H2("FormLabel"),
        html.H3("WithToggletip"),
        carbon_dash.FormLabel(id='formlabel-withtoggletip'),
    ])

stories_dict['node-grid'] = html.Div([
        html.H2("Grid"),
        html.H3("AutoColumns"),
        html.Div(id='templates', children=carbon_dash.FlexGrid(children=carbon_dash.Row(children=[carbon_dash.Column(children=html.Div(children='Span 25%')), carbon_dash.Column(children=html.Div(children='Span 25%')), carbon_dash.Column(children=html.Div(children='Span 25%')), carbon_dash.Column(children=html.Div(children='Span 25%'))]))),
        html.H3("ResponsiveGrid"),
        html.Div(id='templates', children=carbon_dash.FlexGrid(children=carbon_dash.Row(children=[carbon_dash.Column(sm=2, md=4, lg=6, children=html.Div(children=[html.Div(children='Small: Span 2 of 4'), html.Div(children='Medium: Span 4 of 8'), html.Div(children='Large: Span 6 of 16')])), carbon_dash.Column(sm=2, md=2, lg=3, children=html.Div(children=[html.Div(children='Small: Span 2 of 4'), html.Div(children='Medium: Span 2 of 8'), html.Div(children='Large: Span 3 of 16')])), carbon_dash.Column(sm=0, md=2, lg=3, children=html.Div(children=[html.Div(children='Small: Span 0 of 4'), html.Div(children='Medium: Span 2 of 8'), html.Div(children='Large: Span 3 of 16')]))]))),
        html.H3("Offset"),
        html.Div(className='sb-css-grid-container', children=carbon_dash.Grid(children=[carbon_dash.Column(), carbon_dash.Column(), carbon_dash.Column(), carbon_dash.Column(), carbon_dash.Column()])),
        html.H3("Condensed"),
        html.Div(className='sb-css-grid-container', children=carbon_dash.Grid(condensed=True, children=[carbon_dash.Column(sm=4), carbon_dash.Column(sm=4), carbon_dash.Column(sm=4), carbon_dash.Column(sm=4)])),
        html.H3("CondensedColumns"),
        html.Div(id='templates', children=carbon_dash.FlexGrid(children=[carbon_dash.Row(children=[carbon_dash.Column(children=html.Div(children='1/4')), carbon_dash.Column(children=html.Div(children='1/4')), carbon_dash.Column(children=html.Div(children='1/4')), carbon_dash.Column(children=html.Div(children='1/4'))]), carbon_dash.Row(condensed=True, children=[carbon_dash.Column(children=html.Div(children='1/4')), carbon_dash.Column(children=html.Div(children='1/4')), carbon_dash.Column(children=html.Div(children='1/4')), carbon_dash.Column(children=html.Div(children='1/4'))]), carbon_dash.Row(children=[carbon_dash.Column(children=html.Div(children='1/4')), carbon_dash.Column(children=html.Div(children='1/4')), carbon_dash.Column(children=html.Div(children='1/4')), carbon_dash.Column(children=html.Div(children='1/4'))])])),
        html.H3("Narrow"),
        html.Div(className='sb-css-grid-container', children=carbon_dash.Grid(narrow=True, children=[carbon_dash.Column(sm=4), carbon_dash.Column(sm=4), carbon_dash.Column(sm=4), carbon_dash.Column(sm=4)])),
        html.H3("NarrowColumns"),
        html.Div(id='templates', children=carbon_dash.FlexGrid(children=[carbon_dash.Row(children=[carbon_dash.Column(children=html.Div(children='1/4')), carbon_dash.Column(children=html.Div(children='1/4')), carbon_dash.Column(children=html.Div(children='1/4')), carbon_dash.Column(children=html.Div(children='1/4'))]), carbon_dash.Row(narrow=True, children=[carbon_dash.Column(children=html.Div(children='1/4')), carbon_dash.Column(children=html.Div(children='1/4')), carbon_dash.Column(children=html.Div(children='1/4')), carbon_dash.Column(children=html.Div(children='1/4'))]), carbon_dash.Row(children=[carbon_dash.Column(children=html.Div(children='1/4')), carbon_dash.Column(children=html.Div(children='1/4')), carbon_dash.Column(children=html.Div(children='1/4')), carbon_dash.Column(children=html.Div(children='1/4'))])])),
        html.H3("FullWidth"),
        html.Div(className='sb-css-grid-container', children=carbon_dash.Grid(fullWidth=True, children=[carbon_dash.Column(sm=4), carbon_dash.Column(sm=4), carbon_dash.Column(sm=4), carbon_dash.Column(sm=4)])),
        html.H3("MixedGutterModes"),
        html.Div(className='sb-css-grid-container', children=[carbon_dash.Grid(children=carbon_dash.Column(span=8, children=carbon_dash.Grid(children=carbon_dash.Column(span=8, children=carbon_dash.Grid(narrow=True, children=[carbon_dash.Column(children=carbon_dash.ColumnHang(children='Text')), carbon_dash.Column(children=carbon_dash.ColumnHang(children='Text')), carbon_dash.Column(children=carbon_dash.ColumnHang(children='Text')), carbon_dash.Column(children=carbon_dash.ColumnHang(children='Text')), carbon_dash.Column(span=4, children=carbon_dash.Grid(children=[carbon_dash.Column(children='Text'), carbon_dash.Column(children='Text'), carbon_dash.Column(span=2, children=carbon_dash.Grid(condensed=True, children=[carbon_dash.Column(children=carbon_dash.ColumnHang(children='Text')), carbon_dash.Column(children=carbon_dash.ColumnHang(children='Text'))]))]))]))))), carbon_dash.Grid(narrow=True, children=carbon_dash.Column(span=8, children=carbon_dash.Grid(children=[carbon_dash.Column(span=4), carbon_dash.Column(span=4, children=carbon_dash.Grid(narrow=True, children=[carbon_dash.Column(children=carbon_dash.ColumnHang(children='Text')), carbon_dash.Column(children=carbon_dash.ColumnHang(children='Text')), carbon_dash.Column(children=carbon_dash.ColumnHang(children='Text')), carbon_dash.Column(children=carbon_dash.ColumnHang(children='Text'))]))])))]),
        html.H3("Responsive"),
        html.Div(className='sb-css-grid-container', children=carbon_dash.Grid(children=[carbon_dash.Column(sm=2, md=4, lg=6, children=[html.Div(children='Small: Span 2 of 4'), html.Div(children='Medium: Span 4 of 8'), html.Div(children='Large: Span 6 of 16')]), carbon_dash.Column(sm=2, md=2, lg=3, children=[html.Div(children='Small: Span 2 of 4'), html.Div(children='Medium: Span 2 of 8'), html.Div(children='Large: Span 3 of 16')]), carbon_dash.Column(sm=0, md=2, lg=3, children=[html.Div(children='Small: Span 0 of 4'), html.Div(children='Medium: Span 2 of 8'), html.Div(children='Large: Span 3 of 16')]), carbon_dash.Column(sm=0, md=0, lg=4, children=[html.Div(children='Small: Span 0 of 4'), html.Div(children='Medium: Span 0 of 8'), html.Div(children='Large: Span 4 of 16')]), carbon_dash.Column(sm='25%', md='50%', lg='75%', children=[html.Div(children='Small: Span 25%'), html.Div(children='Medium: Span 50%'), html.Div(children='Large: Span 75%')])])),
        html.H3("Subgrid"),
        html.Div(className='sb-css-grid-container', children=[carbon_dash.Grid(children=[carbon_dash.Column(sm=2, md=4, lg=3, children=[html.Div(children='Small: Span 2 of 4'), html.Div(children='Medium: Span 4 of 8'), html.Div(children='Large: Span 3 of 16')]), carbon_dash.Column(sm=2, md=4, lg=10, children=[html.Div(children='Small: Span 2 of 4'), html.Div(children='Medium: Span 4 of 8'), html.Div(children='Large: Span 10 of 16'), carbon_dash.Grid(className='example', children=[carbon_dash.Column(sm=1, md=1, lg=2, children=[html.Div(children='sm='), html.Div(children='md='), html.Div(children='lg=')]), carbon_dash.Column(sm=1, md=1, lg=2, children=[html.Div(children='sm='), html.Div(children='md='), html.Div(children='lg=')]), carbon_dash.Column(sm=0, md=1, lg=1, children=[html.Div(children='sm='), html.Div(children='md='), html.Div(children='lg=')]), carbon_dash.Column(sm=0, md=1, lg=1, children=[html.Div(children='sm='), html.Div(children='md='), html.Div(children='lg=')]), carbon_dash.Column(sm=0, md=0, lg=1, children=[html.Div(children='sm='), html.Div(children='md='), html.Div(children='lg=')]), carbon_dash.Column(sm=0, md=0, lg=1, children=[html.Div(children='sm='), html.Div(children='md='), html.Div(children='lg=')]), carbon_dash.Column(sm=0, md=0, lg=1, children=[html.Div(children='sm='), html.Div(children='md='), html.Div(children='lg=')]), carbon_dash.Column(sm=0, md=0, lg=1, children=[html.Div(children='sm='), html.Div(children='md='), html.Div(children='lg=')])])]), carbon_dash.Column(sm=0, md=0, lg=3, children=[html.Div(children='Small: Span 0 of 4'), html.Div(children='Medium: Span 0 of 8'), html.Div(children='Large: Span 3 of 16')])]), html.Div(children='Wide'), carbon_dash.Grid(children=[carbon_dash.Column(sm=4, md=4, lg=4), carbon_dash.Column(sm=4, md=4, lg=4), carbon_dash.Column(sm=4, md=4, lg=4), carbon_dash.Column(sm=4, md=4, lg=4), carbon_dash.Column(sm=4, md=8, lg=16, children=carbon_dash.Grid(children=[carbon_dash.Column(sm=4, md=4, lg=4), carbon_dash.Column(sm=4, md=4, lg=4), carbon_dash.Column(sm=4, md=4, lg=4), carbon_dash.Column(sm=4, md=4, lg=4)]))]), html.Div(children='Narrow'), carbon_dash.Grid(narrow=True, children=[carbon_dash.Column(sm=4, md=4, lg=4), carbon_dash.Column(sm=4, md=4, lg=4), carbon_dash.Column(sm=4, md=4, lg=4), carbon_dash.Column(sm=4, md=4, lg=4), carbon_dash.Column(sm=4, md=8, lg=16, children=carbon_dash.Grid(narrow=True, children=[carbon_dash.Column(sm=4, md=4, lg=4), carbon_dash.Column(sm=4, md=4, lg=4), carbon_dash.Column(sm=4, md=4, lg=4), carbon_dash.Column(sm=4, md=4, lg=4)]))]), html.Div(children='Condensed'), carbon_dash.Grid(condensed=True, children=[carbon_dash.Column(sm=4, md=4, lg=4), carbon_dash.Column(sm=4, md=4, lg=4), carbon_dash.Column(sm=4, md=4, lg=4), carbon_dash.Column(sm=4, md=4, lg=4), carbon_dash.Column(sm=4, md=8, lg=16, children=carbon_dash.Grid(condensed=True, children=[carbon_dash.Column(sm=4, md=4, lg=4), carbon_dash.Column(sm=4, md=4, lg=4), carbon_dash.Column(sm=4, md=4, lg=4), carbon_dash.Column(sm=4, md=4, lg=4)]))])]),
        html.H3("GridStartEnd"),
        html.Div(className='sb-css-grid-container', children=carbon_dash.Grid(children=[carbon_dash.Column(children='span, start'), carbon_dash.Column(children='span, end'), carbon_dash.Column(children='start, end')])),
        html.H3("WithGridSettings"),
        html.Div(className='sb-css-grid-container', children=carbon_dash.GridSettings(children=carbon_dash.Grid(children=[carbon_dash.Column(sm=4, md=4, lg=4, children=html.Div(children='Column 1')), carbon_dash.Column(sm=4, md=4, lg=4, children=html.Div(children='Column 2')), carbon_dash.Column(sm=4, md=4, lg=4, children=html.Div(children='Column 3')), carbon_dash.Column(sm=4, md=4, lg=4, children=html.Div(children='Column 4'))]))),
    ])

stories_dict['node-heading'] = html.Div([
        html.H2("Heading"),
        html.H3("CustomLevel"),
        carbon_dash.Heading(id='heading-customlevel'),
    ])

stories_dict['node-iconbutton'] = html.Div([
        html.H2("IconButton"),
        html.H3("withBadgeIndicator"),
        html.Div(children=carbon_dash.IconButton(label='Notification', kind='ghost', size='lg', autoAlign=True, children=html.Div())),
    ])

stories_dict['node-inlineloading'] = html.Div([
        html.H2("InlineLoading"),
        html.H3("UxExample"),
        html.Div(),
    ])

stories_dict['node-layer'] = html.Div([
        html.H2("Layer"),
        html.H3("withBackground"),
        carbon_dash.Layer(id='layer-withbackground'),
        html.H3("CustomLevel"),
        carbon_dash.Layer(level=2, children=html.Div()),
        html.H3("UseLayer"),
        carbon_dash.Layer(id='layer-uselayer'),
    ])

stories_dict['node-link'] = html.Div([
        html.H2("Link"),
        html.H3("Inline"),
        carbon_dash.Link(id='link-inline'),
        html.H3("PairedWithIcon"),
        carbon_dash.Link(href='#', children='Carbon Docs'),
    ])

stories_dict['node-menubutton'] = html.Div([
        html.H2("MenuButton"),
        html.H3("FloatingStyles"),
        carbon_dash.MenuButton(label='Actions', children=[carbon_dash.MenuItem(label='First action'), carbon_dash.MenuItem(label='Second action that is a longer item to test overflow and title.'), carbon_dash.MenuItem(label='Third action', disabled=True)]),
        html.H3("ExperimentalAutoAlign"),
        html.Div(children=html.Div(children=carbon_dash.MenuButton(label='Actions', children=[carbon_dash.MenuItem(label='First action'), carbon_dash.MenuItem(label='Second action that is a longer item to test overflow and title.'), carbon_dash.MenuItem(label='Third action', disabled=True)]))),
        html.H3("WithDanger"),
        carbon_dash.MenuButton(label='Actions', children=[carbon_dash.MenuItem(label='First action'), carbon_dash.MenuItem(label='Second action'), carbon_dash.MenuItem(label='Third action'), carbon_dash.MenuItemDivider(), carbon_dash.MenuItem(label='Danger action', kind='danger')]),
        html.H3("WithDividers"),
        carbon_dash.MenuButton(label='Actions', children=[carbon_dash.MenuItem(label='Create service request'), carbon_dash.MenuItem(label='Create work order'), carbon_dash.MenuItemDivider(), carbon_dash.MenuItem(label='Add plan'), carbon_dash.MenuItem(label='Add flag'), carbon_dash.MenuItemDivider(), carbon_dash.MenuItem(label='Edit source location'), carbon_dash.MenuItem(label='Recalculate source')]),
        html.H3("WithIcons"),
        carbon_dash.MenuButton(label='Add', children=[carbon_dash.MenuItem(label='Asset'), carbon_dash.MenuItem(label='User'), carbon_dash.MenuItem(label='User group')]),
        html.H3("WithNestedMenu"),
        carbon_dash.MenuButton(label='Actions', children=[carbon_dash.MenuItem(label='Save', shortcut='⌘S'), carbon_dash.MenuItem(label='Save as', shortcut='⌥⌘S'), carbon_dash.MenuItem(label='Export as', children=[carbon_dash.MenuItem(label='PDF'), carbon_dash.MenuItem(label='JPG'), carbon_dash.MenuItem(label='PNG')]), carbon_dash.MenuItemDivider(), carbon_dash.MenuItem(label='Delete', kind='danger')]),
        html.H3("WithMenuAlignment"),
        carbon_dash.MenuButton(id='menubutton-withmenualignment'),
    ])

stories_dict['node-modal'] = html.Div([
        html.H2("Modal"),
        html.H3("EnableDialogElement"),
        carbon_dash.FeatureFlags(enableDialogElement=True, children=html.Div(children=[carbon_dash.Button(children='Launch modal'), carbon_dash.ClassPrefix(prefix='dialog-refactor', children=html.Div(className='preview-modal', children=carbon_dash.Modal(modalHeading='Add a custom domain', modalLabel='Account resources', primaryButtonText='Add', secondaryButtonText='Cancel', children=[html.Div(children='Custom domains direct requests for your apps in this Cloud\n                Foundry organization to a URL that you own. A custom domain can\n                be a shared domain, a shared subdomain, or a shared domain and\n                host.'), carbon_dash.TextInput(id='text-input-1', labelText='Domain name', placeholder='e.g. github.com'), carbon_dash.Select(id='select-1', defaultValue='us-south', labelText='Region', children=[carbon_dash.SelectItem(value='us-south', text='US South'), carbon_dash.SelectItem(value='us-east', text='US East')]), carbon_dash.Dropdown(id='drop', label='Dropdown', titleText='Dropdown'), carbon_dash.MultiSelect(id='test', label='Multiselect', titleText='Multiselect')])))])),
        html.H3("EnableFocusWrapWithoutSentinels"),
        carbon_dash.FeatureFlags(enableFocusWrapWithoutSentinels=True, children=html.Div(children=[carbon_dash.Button(children='Launch modal'), carbon_dash.ClassPrefix(prefix='dialog-refactor', children=html.Div(className='preview-modal', children=carbon_dash.Modal(modalHeading='Add a custom domain', modalLabel='Account resources', primaryButtonText='Add', secondaryButtonText='Cancel', children=[html.Div(children='Custom domains direct requests for your apps in this Cloud\n                Foundry organization to a URL that you own. A custom domain can\n                be a shared domain, a shared subdomain, or a shared domain and\n                host.'), carbon_dash.TextInput(id='text-input-1', labelText='Domain name', placeholder='e.g. github.com'), carbon_dash.Select(id='select-1', defaultValue='us-south', labelText='Region', children=[carbon_dash.SelectItem(value='us-south', text='US South'), carbon_dash.SelectItem(value='us-east', text='US East')]), carbon_dash.Dropdown(id='drop', label='Dropdown', titleText='Dropdown'), carbon_dash.MultiSelect(id='test', label='Multiselect', titleText='Multiselect')])))])),
        html.H3("FullWidth"),
        carbon_dash.Modal(id='modal-fullwidth'),
        html.H3("DangerModal"),
        carbon_dash.Modal(id='modal-dangermodal'),
        html.H3("WithScrollingContent"),
        carbon_dash.Modal(id='modal-withscrollingcontent'),
        html.H3("WithStateManager"),
        html.Div(),
        html.H3("PassiveModal"),
        carbon_dash.Modal(id='modal-passivemodal'),
        html.H3("WithInlineLoading"),
        carbon_dash.Modal(id='modal-withinlineloading'),
        html.H3("withAILabel"),
        carbon_dash.Modal(id='modal-withailabel'),
        html.H3("EnablePresence"),
        carbon_dash.FeatureFlags(enablePresence=True, children=html.Div(children=[carbon_dash.Button(children='Launch modal'), carbon_dash.ClassPrefix(prefix='dialog-refactor', children=html.Div(className='preview-modal-with-presence', children=carbon_dash.Modal(modalHeading='Add a custom domain', modalLabel='Account resources', primaryButtonText='Add', secondaryButtonText='Cancel', children=[html.Div(children='Custom domains direct requests for your apps in this Cloud\n                Foundry organization to a URL that you own. A custom domain can\n                be a shared domain, a shared subdomain, or a shared domain and\n                host.'), carbon_dash.TextInput(id='text-input-1', labelText='Domain name', placeholder='e.g. github.com'), carbon_dash.Select(id='select-1', defaultValue='us-south', labelText='Region', children=[carbon_dash.SelectItem(value='us-south', text='US South'), carbon_dash.SelectItem(value='us-east', text='US East')]), carbon_dash.Dropdown(id='drop', label='Dropdown', titleText='Dropdown'), carbon_dash.MultiSelect(id='test', label='Multiselect', titleText='Multiselect')])))])),
    ])

stories_dict['node-multiselect'] = html.Div([
        html.H2("MultiSelect"),
        html.H3("FloatingStyles"),
        carbon_dash.MultiSelect(id='carbon-multiselect-example', selectionFeedback='top-after-reopen'),
        html.H3("WithInitialSelectedItems"),
        html.Div(children=carbon_dash.MultiSelect(label='Multiselect Label', id='carbon-multiselect-example-2', titleText='Multiselect title', helperText='This is helper text', selectionFeedback='top-after-reopen')),
        html.H3("Filterable"),
        html.Div(children=carbon_dash.FilterableMultiSelect(id='carbon-multiselect-example-3', titleText='FilterableMultiSelect title', selectionFeedback='top-after-reopen')),
        html.H3("FilterableWithSelectAll"),
        html.Div(children=carbon_dash.FilterableMultiSelect(id='carbon-multiselect-example-3', titleText='FilterableMultiSelect title', selectionFeedback='top-after-reopen')),
        html.H3("WithLayerMultiSelect"),
        html.Div(),
        html.H3("_FilterableWithLayer"),
        html.Div(),
        html.H3("_Controlled"),
        html.Div(children=[carbon_dash.MultiSelect(id='carbon-multiselect-example-controlled', titleText='Multiselect title', label='Multiselect label', selectionFeedback='top-after-reopen'), html.Div(), carbon_dash.ButtonSet(children=[carbon_dash.Button(id='all', children='Select all'), carbon_dash.Button(id='clear', kind='secondary', children='Clear')])]),
        html.H3("SelectAll"),
        html.Div(children=carbon_dash.MultiSelect(id='carbon-multiselect-example', titleText='Multiselect title', helperText='This is helper text', selectionFeedback='top-after-reopen')),
        html.H3("withAILabel"),
        html.Div(children=carbon_dash.MultiSelect(label='Multiselect Label', id='carbon-multiselect-example', titleText='Multiselect title', helperText='This is helper text', selectionFeedback='top-after-reopen')),
        html.H3("FilterableWithAILabel"),
        html.Div(children=carbon_dash.FilterableMultiSelect(id='carbon-multiselect-example', titleText='Multiselect title', selectionFeedback='top-after-reopen')),
        html.H3("ExperimentalAutoAlign"),
        html.Div(children=html.Div(children=carbon_dash.MultiSelect(label='Multiselect Label', id='carbon-multiselect-example', titleText='Multiselect title', helperText='This is helper text', selectionFeedback='top-after-reopen', autoAlign=True))),
        html.H3("withToggletipLabel"),
        html.Div(children=carbon_dash.MultiSelect(label='Multiselect Label', id='carbon-multiselect-example', helperText='This is helper text', selectionFeedback='top-after-reopen')),
        html.H3("SelectAllWithDynamicItems"),
        html.Div(children=[carbon_dash.MultiSelect(id='carbon-multiselect-example', titleText='Multiselect title', helperText='This is helper text', selectionFeedback='top-after-reopen'), carbon_dash.Button(children='Add 2 items to the list')]),
    ])

stories_dict['node-numberinput'] = html.Div([
        html.H2("NumberInput"),
        html.H3("withAILabel"),
        html.Div(children=carbon_dash.NumberInput(value=50, label='NumberInput label', helperText='Optional helper text.', invalidText='Number is not valid')),
        html.H3("WithTypeOfText"),
        carbon_dash.NumberInput(id='default-number-input', inputMode='decimal', defaultValue=50, label='NumberInput label', helperText='Optional helper text.'),
        html.H3("WithTypeOfTextControlled"),
        carbon_dash.NumberInput(id='numberinput-withtypeoftextcontrolled'),
        html.H3("WithTypeOfCustomValidation"),
        carbon_dash.NumberInput(id='numberinput-withtypeofcustomvalidation'),
        html.H3("Skeleton"),
        carbon_dash.NumberInputSkeleton(),
    ])

stories_dict['node-orderedlist'] = html.Div([
        html.H2("OrderedList"),
        html.H3("Nested"),
        carbon_dash.OrderedList(children=[carbon_dash.ListItem(children=['Ordered List level 1', carbon_dash.OrderedList(nested=True, children=[carbon_dash.ListItem(children='Ordered List level 2'), carbon_dash.ListItem(children=['Ordered List level 2', carbon_dash.OrderedList(nested=True, children=[carbon_dash.ListItem(children='Ordered List level 3'), carbon_dash.ListItem(children='Ordered List level 3')])])])]), carbon_dash.ListItem(children='Ordered List level 1'), carbon_dash.ListItem(children='Ordered List level 1')]),
        html.H3("NativeListStyles"),
        carbon_dash.OrderedList(native=True, children=[carbon_dash.ListItem(children='Ordered List level 1'), carbon_dash.ListItem(children='Ordered List level 1'), carbon_dash.ListItem(children='Ordered List level 1'), carbon_dash.ListItem(children=['Ordered List level 1', carbon_dash.OrderedList(nested=True, children=[carbon_dash.ListItem(children='Ordered List level 2'), carbon_dash.ListItem(children='Ordered List level 2'), carbon_dash.ListItem(children='Ordered List level 2'), carbon_dash.ListItem(children='Ordered List level 2')])]), carbon_dash.ListItem(children='Ordered List level 1'), carbon_dash.ListItem(children='Ordered List level 1'), carbon_dash.ListItem(children='Ordered List level 1'), carbon_dash.ListItem(children='Ordered List level 1'), carbon_dash.ListItem(children='Ordered List level 1'), carbon_dash.ListItem(children='Ordered List level 1'), carbon_dash.ListItem(children='Ordered List level 1'), carbon_dash.ListItem(children='Ordered List level 1')]),
    ])

stories_dict['node-overflowmenu'] = html.Div([
        html.H2("OverflowMenu"),
        html.H3("AutoAlign"),
        html.Div(children=html.Div(children=carbon_dash.OverflowMenu(children=[carbon_dash.MenuItem(label='Stop app'), carbon_dash.MenuItem(label='Restart app'), carbon_dash.MenuItem(label='Rename app'), carbon_dash.MenuItem(label='Edit routes and access'), carbon_dash.MenuItemDivider(), carbon_dash.MenuItem(label='Delete app', kind='danger')]))),
        html.H3("Nested"),
        carbon_dash.FeatureFlags(children=carbon_dash.OverflowMenu(children=[carbon_dash.MenuItem(label='Level 1'), carbon_dash.MenuItem(label='Level 1'), carbon_dash.MenuItem(label='Level 1', children=[carbon_dash.MenuItem(label='Level 2', children=[carbon_dash.MenuItem(label='Level 3'), carbon_dash.MenuItem(label='Level 3', children=carbon_dash.MenuItem(label='Level 4'))]), carbon_dash.MenuItem(label='Level 2'), carbon_dash.MenuItem(label='Level 2')]), carbon_dash.MenuItem(label='Level 1')])),
        html.H3("WithMenuAlignment"),
        carbon_dash.OverflowMenu(id='overflowmenu-withmenualignment'),
        html.H3("FloatingStyles"),
        html.Div(children=carbon_dash.OverflowMenu(children=[carbon_dash.MenuItem(label='Stop app'), carbon_dash.MenuItem(label='Restart app'), carbon_dash.MenuItem(label='Rename app'), carbon_dash.MenuItem(label='Edit routes and access'), carbon_dash.MenuItemDivider(), carbon_dash.MenuItem(label='Delete app', kind='danger')])),
        html.H3("RenderCustomIcon"),
        carbon_dash.OverflowMenu(children=[carbon_dash.OverflowMenuItem(itemText='Filter A'), carbon_dash.OverflowMenuItem(itemText='Filter B')]),
    ])

stories_dict['node-pagination'] = html.Div([
        html.H2("Pagination"),
        html.H3("MultiplePaginationComponents"),
        html.Div(children=[carbon_dash.Pagination(), carbon_dash.Pagination()]),
        html.H3("PaginationWithCustomPageSizesLabel"),
        html.Div(children=carbon_dash.Pagination()),
        html.H3("PaginationUnknownPages"),
        html.Div(children=carbon_dash.Pagination(pagesUnknown=True, page=1)),
    ])

stories_dict['node-popover'] = html.Div([
        html.H2("Popover"),
        html.H3("FloatingStyles"),
        html.Div(children=carbon_dash.Popover(children=[html.Div(className='playground-trigger', children=html.Div()), carbon_dash.PopoverContent(className='p-3', children=html.Div(children=[html.Div(className='popover-title', children='This popover uses autoAlign'), html.Div(className='popover-details', children='Scroll the container up, down, left or right to observe how the\n              popover will automatically change its position in attempt to stay\n              within the viewport. This works on initial render in addition to\n              on scroll.')]))])),
        html.H3("TabTip"),
        html.Div(className='popover-tabtip-story', children=[carbon_dash.Popover(isTabTip=True, children=[html.Div(children=html.Div()), carbon_dash.PopoverContent(className='p-3', children=[carbon_dash.RadioButtonGroup(legendText='Row height 1', name='radio-button-group', defaultSelected='small', children=[carbon_dash.RadioButton(labelText='Small', value='small', id='radio-small'), carbon_dash.RadioButton(labelText='Large', value='large', id='radio-large')]), html.Div(), html.Div(children=[html.Div(children='Edit columns'), carbon_dash.Checkbox(defaultChecked=True, labelText='Name', id='checkbox-label-1'), carbon_dash.Checkbox(defaultChecked=True, labelText='Type', id='checkbox-label-2'), carbon_dash.Checkbox(defaultChecked=True, labelText='Location', id='checkbox-label-3')])])]), carbon_dash.Popover(isTabTip=True, children=[html.Div(children=html.Div()), carbon_dash.PopoverContent(className='p-3', children=[carbon_dash.RadioButtonGroup(legendText='Row height 2', name='radio-button-group-2', defaultSelected='small-2', children=[carbon_dash.RadioButton(labelText='Small', value='small-2', id='radio-small-2'), carbon_dash.RadioButton(labelText='Large', value='large-2', id='radio-large-2')]), html.Div(), html.Div(children=[html.Div(children='Testing'), carbon_dash.Checkbox(defaultChecked=True, labelText='Name', id='checkbox-label-8'), carbon_dash.Checkbox(defaultChecked=True, labelText='Type', id='checkbox-label-9'), carbon_dash.Checkbox(defaultChecked=True, labelText='Location', id='checkbox-label-10')])])])]),
        html.H3("ExperimentalAutoAlign"),
        html.Div(children=html.Div(children=carbon_dash.Popover(align='top', autoAlign=True, children=[html.Div(className='playground-trigger', children=html.Div()), carbon_dash.PopoverContent(className='p-3', children=html.Div(children=[html.Div(className='popover-title', children='This popover uses autoAlign'), html.Div(className='popover-details', children='Scroll the container up, down, left or right to observe how the\n                popover will automatically change its position in attempt to\n                stay within the viewport. This works on initial render in\n                addition to on scroll.')]))]))),
        html.H3("ExperimentalAutoAlignBoundary"),
        html.Div(children=[html.Div(), html.Div(children=[carbon_dash.Popover(align='top', autoAlign=True, children=[html.Div(className='playground-trigger', children=html.Div()), carbon_dash.PopoverContent(className='p-3', children=html.Div(children=[html.Div(className='popover-title', children='This popover uses autoAlign'), html.Div(className='popover-details', children='Scroll the container up, down, left or right to observe how the\n                popover will automatically change its position in attempt to\n                stay within the viewport. This works on initial render in\n                addition to on scroll.')]))]), html.Div()])]),
        html.H3("TabTipExperimentalAutoAlign"),
        html.Div(children=html.Div(children=carbon_dash.Popover(align='bottom-right', autoAlign=True, isTabTip=True, children=[html.Div(className='playground-trigger', children=html.Div()), carbon_dash.PopoverContent(className='p-3', children=html.Div(children=[html.Div(className='popover-title', children='This popover uses autoAlign with isTabTip'), html.Div(className='popover-details', children='Scroll the container up, down, left or right to observe how the\n                popover will automatically change its position in attempt to\n                stay within the viewport. This works on initial render in\n                addition to on scroll.')]))]))),
    ])

stories_dict['node-progressbar'] = html.Div([
        html.H2("ProgressBar"),
        html.H3("Indeterminate"),
        carbon_dash.ProgressBar(label='Progress bar label', helperText='Optional helper text'),
        html.H3("Determinate"),
        carbon_dash.ProgressBar(label='Export data'),
        html.H3("_WithLayer"),
        html.Div(children=carbon_dash.ProgressBar(label='Progress bar label', helperText='Optional helper text', value=42)),
    ])

stories_dict['node-progressindicator'] = html.Div([
        html.H2("ProgressIndicator"),
        html.H3("Interactive"),
        carbon_dash.ProgressIndicator(currentIndex=1, children=[carbon_dash.ProgressStep(label='Click me', description='Step 1: Register an onChange event'), carbon_dash.ProgressStep(label='Really long label', description='The progress indicator will listen for clicks on the steps'), carbon_dash.ProgressStep(label='Third step', description='The progress indicator will listen for clicks on the steps')]),
        html.H3("Skeleton"),
        carbon_dash.ProgressIndicatorSkeleton(),
    ])

stories_dict['node-radiobutton'] = html.Div([
        html.H2("RadioButton"),
        html.H3("Vertical"),
        carbon_dash.RadioButtonGroup(legendText='Group label', name='radio-button-vertical-group', defaultSelected='radio-1', orientation='vertical', children=[carbon_dash.RadioButton(labelText='Radio button label', value='radio-1', id='radio-1'), carbon_dash.RadioButton(labelText='Radio button label', value='radio-2', id='radio-2'), carbon_dash.RadioButton(labelText='Radio button label', value='radio-3', id='radio-3', disabled=True)]),
        html.H3("Skeleton"),
        carbon_dash.RadioButtonSkeleton(),
        html.H3("withAILabel"),
        html.Div(className='ai-label-check-radio-container', children=[carbon_dash.RadioButtonGroup(orientation='vertical', legendText='Group label', name='radio-button-group', defaultSelected='radio-1', children=[carbon_dash.RadioButton(labelText='Radio button label', value='radio-1', id='radio-1'), carbon_dash.RadioButton(labelText='Radio button label', value='radio-2', id='radio-2'), carbon_dash.RadioButton(labelText='Radio button label', value='radio-3', id='radio-3')]), carbon_dash.RadioButtonGroup(orientation='vertical', legendText='Group label', name='radio-button-group-2', defaultSelected='radio-4', children=[carbon_dash.RadioButton(labelText='Radio button label', value='radio-4', id='radio-4'), carbon_dash.RadioButton(labelText='Radio button label', value='radio-5', id='radio-5'), carbon_dash.RadioButton(labelText='Radio button label', value='radio-6', id='radio-6')]), carbon_dash.RadioButtonGroup(orientation='vertical', legendText='Group label', name='radio-button-group-3', defaultSelected='radio-7', children=[carbon_dash.RadioButton(labelText='Radio button label', value='radio-7', id='radio-7'), carbon_dash.RadioButton(labelText='Radio button label', value='radio-8', id='radio-8'), carbon_dash.RadioButton(labelText='Radio button label', value='radio-9', id='radio-9')])]),
    ])

stories_dict['node-search'] = html.Div([
        html.H2("Search"),
        html.H3("Disabled"),
        carbon_dash.Search(disabled=True, size='lg', placeholder='Find your items', labelText='Search', closeButtonLabelText='Clear search input', id='search-1'),
        html.H3("Expandable"),
        html.Div(children=carbon_dash.ExpandableSearch(size='lg', labelText='Search', closeButtonLabelText='Clear search input', id='search-expandable-1')),
        html.H3("_WithLayer"),
        html.Div(),
        html.H3("ExpandableWithLayer"),
        html.Div(),
    ])

stories_dict['node-select'] = html.Div([
        html.H2("Select"),
        html.H3("Inline"),
        html.Div(children=carbon_dash.Select(inline=True, id='select-1', labelText='Select an option', helperText='Optional helper text', children=[carbon_dash.SelectItem(value='', text=''), carbon_dash.SelectItem(value='option-1', text='Option 1'), carbon_dash.SelectItem(value='option-2', text='Option 2'), carbon_dash.SelectItem(value='option-3', text='Option 3'), carbon_dash.SelectItem(value='option-4', text='Option 4')])),
        html.H3("Skeleton"),
        carbon_dash.SelectSkeleton(),
        html.H3("_WithLayer"),
        html.Div(),
        html.H3("withAILabel"),
        html.Div(children=carbon_dash.Select(id='select-1', labelText='Select an option', helperText='Optional helper text', children=[carbon_dash.SelectItem(value='', text=''), carbon_dash.SelectItem(value='An example option that is really long to show what should be done to handle long text', text='An example option that is really long to show what should be done to handle long text'), carbon_dash.SelectItem(value='option-2', text='Option 2'), carbon_dash.SelectItem(value='option-3', text='Option 3'), carbon_dash.SelectItem(value='option-4', text='Option 4')])),
    ])

stories_dict['node-slider'] = html.Div([
        html.H2("Slider"),
        html.H3("SliderWithHiddenInputs"),
        carbon_dash.Slider(labelText='Slider label', value=50, min=0, max=100, step=1, stepMultiplier=10, invalidText='Invalid message goes here', hideTextInput=True),
        html.H3("SliderWithCustomValueLabel"),
        carbon_dash.Slider(labelText='Slider label with low/medium/high', value=50, min=0, max=100, stepMultiplier=50, step=1, hideTextInput=True),
        html.H3("ControlledSlider"),
        carbon_dash.Slider(id='slider-controlledslider'),
        html.H3("_WithLayer"),
        html.Div(children=carbon_dash.Slider(labelText='Slider label', value=50, min=0, max=100, step=1, stepMultiplier=10)),
        html.H3("ControlledSliderWithLayer"),
        html.Div(children=[html.Div(children='randomize value'), carbon_dash.Slider(labelText='Slider label', max=100, min=0), html.Div()]),
        html.H3("TwoHandleSlider"),
        carbon_dash.Slider(ariaLabelInput='Lower bound', unstable_ariaLabelInputUpper='Upper bound', labelText='Slider label', value=10, unstable_valueUpper=90, min=0, max=100, step=1, stepMultiplier=10, invalidText='Invalid message goes here'),
        html.H3("TwoHandleSliderWithHiddenInputs"),
        carbon_dash.Slider(ariaLabelInput='Lower bound', unstable_ariaLabelInputUpper='Upper bound', labelText='Slider label', value=10, unstable_valueUpper=90, min=0, max=100, step=1, stepMultiplier=10, invalidText='Invalid message goes here', hideTextInput=True),
        html.H3("Skeleton"),
        carbon_dash.SliderSkeleton(),
        html.H3("TwoHandleSkeleton"),
        carbon_dash.SliderSkeleton(twoHandles=True),
    ])

stories_dict['node-stack'] = html.Div([
        html.H2("Stack"),
        html.H3("Horizontal"),
        carbon_dash.Stack(gap=6, orientation='horizontal', children=[html.Div(children='Item 1'), html.Div(children='Item 2'), html.Div(children='Item 3')]),
    ])

stories_dict['node-tabs'] = html.Div([
        html.H2("Tabs"),
        html.H3("Dismissable"),
        carbon_dash.Tabs(id='tabs-dismissable'),
        html.H3("DismissableContained"),
        carbon_dash.Tabs(id='tabs-dismissablecontained'),
        html.H3("DismissableWithIcons"),
        carbon_dash.Tabs(id='tabs-dismissablewithicons'),
        html.H3("WithIcons"),
        carbon_dash.Tabs(children=[carbon_dash.TabList(activation='manual', children=[carbon_dash.Tab(children='Dashboard'), carbon_dash.Tab(children='Monitoring'), carbon_dash.Tab(children='Activity'), carbon_dash.Tab(children='Analyze'), carbon_dash.Tab(disabled=True, children='Settings')]), carbon_dash.TabPanels(children=[carbon_dash.TabPanel(children='Tab Panel 1'), carbon_dash.TabPanel(children=html.Div(children=[html.Div(children='Validation example'), carbon_dash.Checkbox(id='cb', labelText='Accept privacy policy'), carbon_dash.Button(type='submit', children='Submit'), carbon_dash.TextInput(type='text', labelText='Text input label', helperText='Optional help text', id='text-input-1')])), carbon_dash.TabPanel(children='Tab Panel 3'), carbon_dash.TabPanel(children='Tab Panel 4'), carbon_dash.TabPanel(children='Tab Panel 5')])]),
        html.H3("Manual"),
        carbon_dash.Tabs(children=[carbon_dash.TabList(activation='manual', children=[carbon_dash.Tab(children='Dashboard'), carbon_dash.Tab(children='Monitoring'), carbon_dash.Tab(children='Activity'), carbon_dash.Tab(children='Analyze'), carbon_dash.Tab(disabled=True, children='Settings')]), carbon_dash.TabPanels(children=[carbon_dash.TabPanel(children='Tab Panel 1'), carbon_dash.TabPanel(children=html.Div(children=[html.Div(children='Validation example'), carbon_dash.Checkbox(id='cb', labelText='Accept privacy policy'), carbon_dash.Button(type='submit', children='Submit'), carbon_dash.TextInput(type='text', labelText='Text input label', helperText='Optional help text', id='text-input-1')])), carbon_dash.TabPanel(children='Tab Panel 3'), carbon_dash.TabPanel(children='Tab Panel 4'), carbon_dash.TabPanel(children='Tab Panel 5')])]),
        html.H3("Icon20Only"),
        carbon_dash.Tabs(children=[carbon_dash.TabList(iconSize='lg', children=[carbon_dash.IconTab(label='Analyze', children=html.Div()), carbon_dash.IconTab(label='Activity', children=html.Div()), carbon_dash.IconTab(label='New Notifications', children=html.Div()), carbon_dash.IconTab(label='Chat', children=html.Div())]), carbon_dash.TabPanels(children=[carbon_dash.TabPanel(children='Tab Panel 1'), carbon_dash.TabPanel(children='Tab Panel 2'), carbon_dash.TabPanel(children='Tab Panel 3'), carbon_dash.TabPanel(children='Tab Panel 4')])]),
        html.H3("IconOnly"),
        carbon_dash.Tabs(children=[carbon_dash.TabList(iconSize='default', children=[carbon_dash.IconTab(label='Analyze', children=html.Div()), carbon_dash.IconTab(label='Activity', children=html.Div()), carbon_dash.IconTab(label='New Notifications', children=html.Div()), carbon_dash.IconTab(label='Chat', children=html.Div())]), carbon_dash.TabPanels(children=[carbon_dash.TabPanel(children='Tab Panel 1'), carbon_dash.TabPanel(children='Tab Panel 2'), carbon_dash.TabPanel(children='Tab Panel 3'), carbon_dash.TabPanel(children='Tab Panel 4')])]),
        html.H3("Contained"),
        carbon_dash.Tabs(children=[carbon_dash.TabList(contained=True, children=[carbon_dash.Tab(children='Dashboard'), carbon_dash.Tab(children='Monitoring'), carbon_dash.Tab(children='Activity'), carbon_dash.Tab(children='Analyze'), carbon_dash.Tab(disabled=True, children='Settings')]), carbon_dash.TabPanels(children=[carbon_dash.TabPanel(children='Tab Panel 1'), carbon_dash.TabPanel(children=carbon_dash.Layer(children=html.Div(children=[html.Div(children='Validation example'), carbon_dash.Checkbox(id='cb', labelText='Accept privacy policy'), carbon_dash.Button(type='submit', children='Submit'), carbon_dash.TextInput(type='text', labelText='Text input label', helperText='Optional help text')]))), carbon_dash.TabPanel(children='Tab Panel 3'), carbon_dash.TabPanel(children='Tab Panel 4'), carbon_dash.TabPanel(children='Tab Panel 5')])]),
        html.H3("ContainedWithIcons"),
        carbon_dash.Tabs(children=[carbon_dash.TabList(contained=True, children=[carbon_dash.Tab(children='Dashboard'), carbon_dash.Tab(children='Monitoring'), carbon_dash.Tab(children='Activity'), carbon_dash.Tab(children='Analyze'), carbon_dash.Tab(disabled=True, children='Settings')]), carbon_dash.TabPanels(children=[carbon_dash.TabPanel(children='Tab Panel 1'), carbon_dash.TabPanel(children=carbon_dash.Layer(children=html.Div(children=[html.Div(children='Validation example'), carbon_dash.Checkbox(id='cb', labelText='Accept privacy policy'), carbon_dash.Button(type='submit', children='Submit'), carbon_dash.TextInput(type='text', labelText='Text input label', helperText='Optional help text')]))), carbon_dash.TabPanel(children='Tab Panel 3'), carbon_dash.TabPanel(children='Tab Panel 4'), carbon_dash.TabPanel(children='Tab Panel 5')])]),
        html.H3("ContainedWithSecondaryLabels"),
        carbon_dash.Tabs(children=[carbon_dash.TabList(contained=True, children=[carbon_dash.Tab(secondaryLabel='(21/25)', children='Engage'), carbon_dash.Tab(secondaryLabel='(12/16)', children='Analyze'), carbon_dash.Tab(secondaryLabel='(0/7)', children='Remediate'), carbon_dash.Tab(secondaryLabel='(4/12)', children='Assets'), carbon_dash.Tab(disabled=True, secondaryLabel='(0/10)', children='Monitoring')]), carbon_dash.TabPanels(children=[carbon_dash.TabPanel(children='Tab Panel 1'), carbon_dash.TabPanel(children=carbon_dash.Layer(children=html.Div(children=[html.Div(children='Validation example'), carbon_dash.Checkbox(id='cb', labelText='Accept privacy policy'), carbon_dash.Button(type='submit', children='Submit'), carbon_dash.TextInput(type='text', labelText='Text input label', helperText='Optional help text')]))), carbon_dash.TabPanel(children='Tab Panel 3'), carbon_dash.TabPanel(children='Tab Panel 4'), carbon_dash.TabPanel(children='Tab Panel 5')])]),
        html.H3("ContainedWithSecondaryLabelsAndIcons"),
        carbon_dash.Tabs(children=[carbon_dash.TabList(contained=True, children=[carbon_dash.Tab(secondaryLabel='(21/25', children='Engage'), carbon_dash.Tab(secondaryLabel='(12/16)', children='Analyze'), carbon_dash.Tab(disabled=True, secondaryLabel='(0/7)', children='Remediate'), carbon_dash.Tab(secondaryLabel='(4/12)', children='Assets'), carbon_dash.Tab(secondaryLabel='(1/23)', children='Monitoring')]), carbon_dash.TabPanels(children=[carbon_dash.TabPanel(children='Tab Panel 1'), carbon_dash.TabPanel(children=carbon_dash.Layer(children=html.Div(children=[html.Div(children='Validation example'), carbon_dash.Checkbox(id='cb', labelText='Accept privacy policy'), carbon_dash.Button(type='submit', children='Submit'), carbon_dash.TextInput(type='text', labelText='Text input label', helperText='Optional help text')]))), carbon_dash.TabPanel(children='Tab Panel 3'), carbon_dash.TabPanel(children='Tab Panel 4'), carbon_dash.TabPanel(children='Tab Panel 5')])]),
        html.H3("ContainedFullWidth"),
        carbon_dash.Grid(condensed=True, children=carbon_dash.Column(lg=16, md=8, sm=4, children=carbon_dash.Tabs(children=[carbon_dash.TabList(contained=True, fullWidth=True, children=[carbon_dash.Tab(children='TLS'), carbon_dash.Tab(children='Origin'), carbon_dash.Tab(disabled=True, children='Rate limiting'), carbon_dash.Tab(children='WAF'), carbon_dash.Tab(children='IP Firewall'), carbon_dash.Tab(children='Firewall rules'), carbon_dash.Tab(children='Range'), carbon_dash.Tab(children='Mutual TLS')]), carbon_dash.TabPanels(children=[carbon_dash.TabPanel(children='Tab Panel 1'), carbon_dash.TabPanel(children=carbon_dash.Layer(children=html.Div(children=[html.Div(children='Validation example'), carbon_dash.Checkbox(id='cb', labelText='Accept privacy policy'), carbon_dash.Button(type='submit', children='Submit'), carbon_dash.TextInput(type='text', labelText='Text input label', helperText='Optional help text')]))), carbon_dash.TabPanel(children='Tab Panel 3'), carbon_dash.TabPanel(children='Tab Panel 4'), carbon_dash.TabPanel(children='Tab Panel 5'), carbon_dash.TabPanel(children='Tab Panel 6'), carbon_dash.TabPanel(children='Tab Panel 7'), carbon_dash.TabPanel(children='Tab Panel 8')])]))),
        html.H3("Vertical"),
        carbon_dash.TabsVertical(children=[carbon_dash.TabListVertical(children=[carbon_dash.Tab(children='Dashboard'), carbon_dash.Tab(children='Extra long label that will go two lines then truncate when it goes\n          beyond the Tab length'), carbon_dash.Tab(children='Activity'), carbon_dash.Tab(children='Analyze'), carbon_dash.Tab(children='Investigate'), carbon_dash.Tab(children='Learn'), carbon_dash.Tab(disabled=True, children='Settings')]), carbon_dash.TabPanels(children=[carbon_dash.TabPanel(children='Tab Panel 1'), carbon_dash.TabPanel(children=carbon_dash.Layer(children=html.Div(children=carbon_dash.Stack(gap=7, children=[carbon_dash.TextInput(id='one', labelText='First Name'), carbon_dash.TextInput(id='three', labelText='Middle Initial'), carbon_dash.TextInput(id='two', labelText='Last Name'), carbon_dash.RadioButtonGroup(legendText='Radio button heading', name='formgroup-default-radio-button-group', defaultSelected='radio-1', children=[carbon_dash.RadioButton(labelText='Option 1', value='radio-1', id='radio-1'), carbon_dash.RadioButton(labelText='Option 2', value='radio-2', id='radio-2'), carbon_dash.RadioButton(labelText='Option 3', value='radio-3', id='radio-3')]), carbon_dash.Checkbox(id='checkbox-label-1'), carbon_dash.Checkbox(id='checkbox-label-2'), carbon_dash.Button(children='Submit')])))), carbon_dash.TabPanel(children='Tab Panel 3'), carbon_dash.TabPanel(children='Tab Panel 4'), carbon_dash.TabPanel(children='Tab Panel 5'), carbon_dash.TabPanel(children='Tab Panel 6'), carbon_dash.TabPanel(children='Tab Panel 7')])]),
        html.H3("Skeleton"),
        html.Div(children=carbon_dash.TabsSkeleton()),
        html.H3("Icon20OnlyVisualSnapshots"),
        carbon_dash.Tabs(children=[carbon_dash.TabList(iconSize='lg', children=[carbon_dash.IconTab(label='Analyze', children=html.Div()), carbon_dash.IconTab(label='Activity', children=html.Div()), carbon_dash.IconTab(label='New Notifications', children=html.Div()), carbon_dash.IconTab(label='Chat', children=html.Div())]), carbon_dash.TabPanels(children=[carbon_dash.TabPanel(children='Tab Panel 1'), carbon_dash.TabPanel(children='Tab Panel 2'), carbon_dash.TabPanel(children='Tab Panel 3'), carbon_dash.TabPanel(children='Tab Panel 4')])]),
        html.H3("IconOnlyVisualSnapshots"),
        carbon_dash.Tabs(children=[carbon_dash.TabList(iconSize='default', children=[carbon_dash.IconTab(label='Analyze', children=html.Div()), carbon_dash.IconTab(label='Activity', children=html.Div()), carbon_dash.IconTab(label='New Notifications', children=html.Div()), carbon_dash.IconTab(label='Chat', children=html.Div())]), carbon_dash.TabPanels(children=[carbon_dash.TabPanel(children='Tab Panel 1'), carbon_dash.TabPanel(children='Tab Panel 2'), carbon_dash.TabPanel(children='Tab Panel 3'), carbon_dash.TabPanel(children='Tab Panel 4')])]),
    ])

stories_dict['node-tag'] = html.Div([
        html.H2("Tag"),
        html.H3("Selectable"),
        html.Div(role='group'),
        html.H3("Operational"),
        carbon_dash.Tag(id='tag-operational'),
        html.H3("Dismissible"),
        carbon_dash.Tag(id='tag-dismissible'),
        html.H3("ReadOnly"),
        carbon_dash.Tag(id='tag-readonly'),
        html.H3("Skeleton"),
        html.Div(children=carbon_dash.TagSkeleton()),
        html.H3("withAILabel"),
        html.Div(children=[carbon_dash.Tag(className='some-class', type='red', title='Clear Filter'), carbon_dash.DismissibleTag(className='some-class', type='purple', title='Clear Filter'), carbon_dash.Tag(className='some-class', type='blue', title='Clear Filter'), carbon_dash.DismissibleTag(className='some-class', type='green', title='Clear Filter')]),
    ])

stories_dict['node-textarea'] = html.Div([
        html.H2("TextArea"),
        html.H3("_WithLayer"),
        html.Div(),
        html.H3("withAILabel"),
        carbon_dash.TextArea(labelText='Text Area label', helperText='Optional helper text', rows=4, id='text-area-5'),
        html.H3("Skeleton"),
        carbon_dash.TextAreaSkeleton(),
    ])

stories_dict['node-textinput'] = html.Div([
        html.H2("TextInput"),
        html.H3("Fluid"),
        html.Div(children=carbon_dash.FluidForm(children=carbon_dash.TextInput())),
        html.H3("ReadOnly"),
        html.Div(children=carbon_dash.TextInput()),
        html.H3("_WithLayer"),
        html.Div(),
        html.H3("withAILabel"),
        html.Div(children=carbon_dash.TextInput(type='text', labelText='Text input label', helperText='Optional help text', id='text-input-ai-label')),
        html.H3("Skeleton"),
        carbon_dash.TextInputSkeleton(),
        html.H3("TestInvalidTextNoOverlap"),
        html.Div(children=[carbon_dash.TextInput(labelText='test invalid text, the invalid text should not overlap', invalid=True, invalidText='invalid text, this should not overlap with the component below', id='text-input-1', type='text'), carbon_dash.TextInput(labelText='test label', id='text-input-2', type='text')]),
    ])

stories_dict['node-theme'] = html.Div([
        html.H2("Theme"),
        html.H3("UseTheme"),
        html.Div(children=[html.Div(className='theme-section', children=html.Div()), carbon_dash.Theme(theme='g100', children=html.Div(className='theme-section', children=html.Div()))]),
        html.H3("UsePrefersDarkScheme"),
        carbon_dash.Theme(children=[html.Div(className='theme-section', children=html.Div(children=['usePrefersDarkScheme() is', '. Theme\n          set to `', '`.'])), carbon_dash.Theme(children=html.Div(className='theme-section', children=html.Div(children=['usePrefersDarkScheme() is', '. An\n            alternative theme set of `', '`.']))), carbon_dash.Theme(children=html.Div(className='theme-section', children=html.Div(children=['usePrefersDarkScheme() is', '.\n            Theme set to `', '`.']))), carbon_dash.Theme(children=html.Div(className='theme-section', children=html.Div(children=['usePrefersDarkScheme() is', '. An\n            alternative theme set of `', '`.'])))]),
        html.H3("_WithLayer"),
        carbon_dash.VStack(gap=7),
    ])

stories_dict['node-tile'] = html.Div([
        html.H2("Tile"),
        html.H3("Clickable"),
        carbon_dash.ClickableTile(id='clickable-tile-1', href='https://www.carbondesignsystem.com/', children='Clickable Tile'),
        html.H3("ClickableWithLayer"),
        html.Div(),
        html.H3("Selectable"),
        carbon_dash.SelectableTile(id='selectable-tile-1', children='Selectable'),
        html.H3("MultiSelect"),
        html.Div(role='group', children=[carbon_dash.SelectableTile(id='selectable-tile-1', name='tiles', children='Option 1'), carbon_dash.SelectableTile(id='selectable-tile-2', name='tiles', children='Option 2'), carbon_dash.SelectableTile(id='selectable-tile-3', name='tiles', children='Option 3')]),
        html.H3("Radio"),
        carbon_dash.TileGroup(defaultSelected='default-selected', legend='Radio Tile Group', name='radio tile group', children=[carbon_dash.RadioTile(id='radio-tile-1', value='standard', children='Option 1'), carbon_dash.RadioTile(id='radio-tile-2', value='default-selected', children='Option 2'), carbon_dash.RadioTile(id='radio-tile-3', value='selected', children='Option 3')]),
        html.H3("RadioWithLayer"),
        html.Div(),
        html.H3("Expandable"),
        html.Div(children=carbon_dash.ExpandableTile(id='expandable-tile-1', tileCollapsedIconText='Interact to Expand tile', tileExpandedIconText='Interact to Collapse tile', children=[carbon_dash.TileAboveTheFoldContent(children=html.Div(children='Above the fold content here')), carbon_dash.TileBelowTheFoldContent(children=html.Div(children='Below the fold content here'))])),
        html.H3("ExpandableWithInteractive"),
        html.Div(children=carbon_dash.ExpandableTile(id='expandable-tile-1', tileCollapsedIconText='Interact to Expand tile', tileExpandedIconText='Interact to Collapse tile', children=[carbon_dash.TileAboveTheFoldContent(children=html.Div(children=['Above the fold content here', html.Div(children=carbon_dash.Button(children='Example'))])), carbon_dash.TileBelowTheFoldContent(children=html.Div(children=['Below the fold content here', carbon_dash.TextInput(id='test2', invalidText='A valid value is required')]))])),
        html.H3("ExpandableWithLayer"),
        html.Div(),
        html.H3("_WithAILabel"),
        carbon_dash.Tile(id='tile-_withailabel'),
        html.H3("DefaultWithLayer"),
        html.Div(),
        html.H3("ClickableWithCustomIcon"),
        carbon_dash.ClickableTile(id='clickable-tile-1', href='https://www.carbondesignsystem.com/', children='Clickable Tile'),
        html.H3("withAILabel"),
        carbon_dash.Tile(id='tile-withailabel'),
    ])

stories_dict['node-timepicker'] = html.Div([
        html.H2("TimePicker"),
        html.H3("_WithLayer"),
        html.Div(),
    ])

stories_dict['node-toggle'] = html.Div([
        html.H2("Toggle"),
        html.H3("_Toggle"),
        html.Div(children=carbon_dash.Toggle(labelText='Label', labelA='Off', labelB='On', defaultToggled=True, id='toggle-3')),
        html.H3("SmallToggle"),
        carbon_dash.Toggle(size='sm', labelText='Label', labelA='Off', labelB='On', defaultToggled=True, id='toggle-2'),
        html.H3("WithAccessibleLabels"),
        carbon_dash.VStack(gap=7, children=[carbon_dash.Toggle(id='toggle-4', labelText='Label'), carbon_dash.Toggle(id='toggle-5', labelText='Label', hideLabel=True), html.Div(children=[html.Div(id='toggle-6-label', children='Internal aria-label toggle'), carbon_dash.Toggle(id='toggle-6')]), html.Div(children=[html.Div(id='toggle-7-label', children='External toggle label'), carbon_dash.Toggle(id='toggle-7')])]),
        html.H3("Skeleton"),
        html.Div(children=carbon_dash.ToggleSkeleton()),
    ])

stories_dict['node-toggletip'] = html.Div([
        html.H2("Toggletip"),
        html.H3("FloatingStyles"),
        html.Div(children=[carbon_dash.ToggletipLabel(children='Toggletip label'), carbon_dash.Toggletip(defaultOpen=True, children=[carbon_dash.ToggletipButton(label='Show information', children=html.Div()), carbon_dash.ToggletipContent(children=[html.Div(children='Scroll the container up, down, left or right to observe how the\n            Toggletip will automatically change its position in attempt to stay\n            within the viewport. This works on initial render in addition to on\n            scroll.'), carbon_dash.ToggletipActions(children=[carbon_dash.Link(href='#', children='Link action'), carbon_dash.Button(size='sm', children='Button')])])])]),
        html.H3("ExperimentalAutoAlign"),
        html.Div(children=html.Div(children=[carbon_dash.ToggletipLabel(children='Toggletip label'), carbon_dash.Toggletip(align='bottom', autoAlign=True, defaultOpen=True, children=[carbon_dash.ToggletipButton(label='Show information', children=html.Div()), carbon_dash.ToggletipContent(children=[html.Div(children='Scroll the container up, down, left or right to observe how the\n              Toggletip will automatically change its position in attempt to\n              stay within the viewport. This works on initial render in addition\n              to on scroll.'), carbon_dash.ToggletipActions(children=[carbon_dash.Link(href='#', children='Link action'), carbon_dash.Button(size='sm', children='Button')])])])])),
    ])

stories_dict['node-tooltip'] = html.Div([
        html.H2("Tooltip"),
        html.H3("WithLargeText"),
        html.Div(children=['Custom domains direct requests for your apps in this Cloud Foundry\n      organization to a', ' ', carbon_dash.DefinitionTooltip(openOnHover=True, children='URL that you own. A custom domain can be a shared domain,'), ' ', 'a shared subdomain, or a shared domain and host.']),
        html.H3("FloatingStyles"),
        html.Div(children=carbon_dash.Tooltip(children=html.Div(className='sb-tooltip-trigger', children=html.Div()))),
        html.H3("Alignment"),
        carbon_dash.Tooltip(label='Tooltip alignment', align='bottom-left', children=carbon_dash.Button(children='This button has a tooltip')),
        html.H3("ExperimentalAutoAlign"),
        html.Div(children=html.Div(children=carbon_dash.Tooltip(align='top', children=carbon_dash.Button(children='This button has a tooltip')))),
        html.H3("Duration"),
        carbon_dash.Tooltip(label='Label one', enterDelayMs=0, leaveDelayMs=300, children=carbon_dash.Button(children='This button has a tooltip')),
    ])

stories_dict['node-treeview'] = html.Div([
        html.H2("TreeView"),
        html.H3("WithIcons"),
        carbon_dash.TreeView(label='Tree View'),
        html.H3("WithLinks"),
        html.Div(id='page-body', children=[html.Div(), html.Div(children=html.Div(children='The current page is:'))]),
        html.H3("WithControlledExpansion"),
        carbon_dash.TreeView(id='treeview-withcontrolledexpansion'),
        html.H3("WithComplexNesting"),
        carbon_dash.TreeView(label='Tree View with Complex Nesting', children=[carbon_dash.TreeNode(id='1', value='A.I.', label='A.I.', isExpanded=True, children=[html.Div(children=carbon_dash.TreeNode(id='1-1', value='Sub 1', label='Sub 1 (in a div)')), carbon_dash.TreeNode(id='1-2', value='Sub 2', label='Sub 2 (direct child)', children=carbon_dash.TreeNode(id='1-2-1', value='Sub 2.1', label='Sub 2.1'))]), carbon_dash.TreeNode(id='2', value='Analytics', label='Analytics', isExpanded=True, children=html.Div()), carbon_dash.TreeNode(id='3', value='Trust', label='Trust')]),
    ])

stories_dict['node-unorderedlist'] = html.Div([
        html.H2("UnorderedList"),
        html.H3("Nested"),
        carbon_dash.UnorderedList(children=[carbon_dash.ListItem(children=['Unordered List level 1', carbon_dash.UnorderedList(nested=True, children=[carbon_dash.ListItem(children='Unordered List level 2'), carbon_dash.ListItem(children=['Unordered List level 2', carbon_dash.UnorderedList(nested=True, children=[carbon_dash.ListItem(children='Unordered List level 2'), carbon_dash.ListItem(children='Unordered List level 2')])])])]), carbon_dash.ListItem(children='Unordered List level 1'), carbon_dash.ListItem(children='Unordered List level 1')]),
    ])


app.layout = html.Div([
    html.Div([
        carbon_dash.TreeView(
            id='component-tree',
            label='Carbon Components',
            children=[
                carbon_dash.TreeNode(
                    id='node-components',
                    label='Components',
                    isExpanded=True,
                    children=[
                        carbon_dash.TreeNode(
                            id='node-ailabel',
                            label='AILabel',
                            value='AILabel'
                        ),
                        carbon_dash.TreeNode(
                            id='node-accordion',
                            label='Accordion',
                            value='Accordion'
                        ),
                        carbon_dash.TreeNode(
                            id='node-breadcrumb',
                            label='Breadcrumb',
                            value='Breadcrumb'
                        ),
                        carbon_dash.TreeNode(
                            id='node-button',
                            label='Button',
                            value='Button'
                        ),
                        carbon_dash.TreeNode(
                            id='node-buttonset',
                            label='ButtonSet',
                            value='ButtonSet'
                        ),
                        carbon_dash.TreeNode(
                            id='node-checkbox',
                            label='Checkbox',
                            value='Checkbox'
                        ),
                        carbon_dash.TreeNode(
                            id='node-codesnippet',
                            label='CodeSnippet',
                            value='CodeSnippet'
                        ),
                        carbon_dash.TreeNode(
                            id='node-combobox',
                            label='ComboBox',
                            value='ComboBox'
                        ),
                        carbon_dash.TreeNode(
                            id='node-combobutton',
                            label='ComboButton',
                            value='ComboButton'
                        ),
                        carbon_dash.TreeNode(
                            id='node-composedmodal',
                            label='ComposedModal',
                            value='ComposedModal'
                        ),
                        carbon_dash.TreeNode(
                            id='node-containedlist',
                            label='ContainedList',
                            value='ContainedList'
                        ),
                        carbon_dash.TreeNode(
                            id='node-contentswitcher',
                            label='ContentSwitcher',
                            value='ContentSwitcher'
                        ),
                        carbon_dash.TreeNode(
                            id='node-datatable',
                            label='DataTable',
                            value='DataTable'
                        ),
                        carbon_dash.TreeNode(
                            id='node-datatableskeleton',
                            label='DataTableSkeleton',
                            value='DataTableSkeleton'
                        ),
                        carbon_dash.TreeNode(
                            id='node-datepicker',
                            label='DatePicker',
                            value='DatePicker'
                        ),
                        carbon_dash.TreeNode(
                            id='node-dropdown',
                            label='Dropdown',
                            value='Dropdown'
                        ),
                        carbon_dash.TreeNode(
                            id='node-errorboundary',
                            label='ErrorBoundary',
                            value='ErrorBoundary'
                        ),
                        carbon_dash.TreeNode(
                            id='node-fileuploader',
                            label='FileUploader',
                            value='FileUploader'
                        ),
                        carbon_dash.TreeNode(
                            id='node-fluidcombobox',
                            label='FluidComboBox',
                            value='FluidComboBox'
                        ),
                        carbon_dash.TreeNode(
                            id='node-fluiddatepicker',
                            label='FluidDatePicker',
                            value='FluidDatePicker'
                        ),
                        carbon_dash.TreeNode(
                            id='node-fluiddropdown',
                            label='FluidDropdown',
                            value='FluidDropdown'
                        ),
                        carbon_dash.TreeNode(
                            id='node-fluidmultiselect',
                            label='FluidMultiSelect',
                            value='FluidMultiSelect'
                        ),
                        carbon_dash.TreeNode(
                            id='node-fluidnumberinput',
                            label='FluidNumberInput',
                            value='FluidNumberInput'
                        ),
                        carbon_dash.TreeNode(
                            id='node-fluidsearch',
                            label='FluidSearch',
                            value='FluidSearch'
                        ),
                        carbon_dash.TreeNode(
                            id='node-fluidselect',
                            label='FluidSelect',
                            value='FluidSelect'
                        ),
                        carbon_dash.TreeNode(
                            id='node-fluidtextarea',
                            label='FluidTextArea',
                            value='FluidTextArea'
                        ),
                        carbon_dash.TreeNode(
                            id='node-fluidtextinput',
                            label='FluidTextInput',
                            value='FluidTextInput'
                        ),
                        carbon_dash.TreeNode(
                            id='node-fluidtimepicker',
                            label='FluidTimePicker',
                            value='FluidTimePicker'
                        ),
                        carbon_dash.TreeNode(
                            id='node-form',
                            label='Form',
                            value='Form'
                        ),
                        carbon_dash.TreeNode(
                            id='node-formlabel',
                            label='FormLabel',
                            value='FormLabel'
                        ),
                        carbon_dash.TreeNode(
                            id='node-grid',
                            label='Grid',
                            value='Grid'
                        ),
                        carbon_dash.TreeNode(
                            id='node-heading',
                            label='Heading',
                            value='Heading'
                        ),
                        carbon_dash.TreeNode(
                            id='node-iconbutton',
                            label='IconButton',
                            value='IconButton'
                        ),
                        carbon_dash.TreeNode(
                            id='node-inlineloading',
                            label='InlineLoading',
                            value='InlineLoading'
                        ),
                        carbon_dash.TreeNode(
                            id='node-layer',
                            label='Layer',
                            value='Layer'
                        ),
                        carbon_dash.TreeNode(
                            id='node-link',
                            label='Link',
                            value='Link'
                        ),
                        carbon_dash.TreeNode(
                            id='node-menubutton',
                            label='MenuButton',
                            value='MenuButton'
                        ),
                        carbon_dash.TreeNode(
                            id='node-modal',
                            label='Modal',
                            value='Modal'
                        ),
                        carbon_dash.TreeNode(
                            id='node-multiselect',
                            label='MultiSelect',
                            value='MultiSelect'
                        ),
                        carbon_dash.TreeNode(
                            id='node-numberinput',
                            label='NumberInput',
                            value='NumberInput'
                        ),
                        carbon_dash.TreeNode(
                            id='node-orderedlist',
                            label='OrderedList',
                            value='OrderedList'
                        ),
                        carbon_dash.TreeNode(
                            id='node-overflowmenu',
                            label='OverflowMenu',
                            value='OverflowMenu'
                        ),
                        carbon_dash.TreeNode(
                            id='node-pagination',
                            label='Pagination',
                            value='Pagination'
                        ),
                        carbon_dash.TreeNode(
                            id='node-popover',
                            label='Popover',
                            value='Popover'
                        ),
                        carbon_dash.TreeNode(
                            id='node-progressbar',
                            label='ProgressBar',
                            value='ProgressBar'
                        ),
                        carbon_dash.TreeNode(
                            id='node-progressindicator',
                            label='ProgressIndicator',
                            value='ProgressIndicator'
                        ),
                        carbon_dash.TreeNode(
                            id='node-radiobutton',
                            label='RadioButton',
                            value='RadioButton'
                        ),
                        carbon_dash.TreeNode(
                            id='node-search',
                            label='Search',
                            value='Search'
                        ),
                        carbon_dash.TreeNode(
                            id='node-select',
                            label='Select',
                            value='Select'
                        ),
                        carbon_dash.TreeNode(
                            id='node-slider',
                            label='Slider',
                            value='Slider'
                        ),
                        carbon_dash.TreeNode(
                            id='node-stack',
                            label='Stack',
                            value='Stack'
                        ),
                        carbon_dash.TreeNode(
                            id='node-tabs',
                            label='Tabs',
                            value='Tabs'
                        ),
                        carbon_dash.TreeNode(
                            id='node-tag',
                            label='Tag',
                            value='Tag'
                        ),
                        carbon_dash.TreeNode(
                            id='node-textarea',
                            label='TextArea',
                            value='TextArea'
                        ),
                        carbon_dash.TreeNode(
                            id='node-textinput',
                            label='TextInput',
                            value='TextInput'
                        ),
                        carbon_dash.TreeNode(
                            id='node-theme',
                            label='Theme',
                            value='Theme'
                        ),
                        carbon_dash.TreeNode(
                            id='node-tile',
                            label='Tile',
                            value='Tile'
                        ),
                        carbon_dash.TreeNode(
                            id='node-timepicker',
                            label='TimePicker',
                            value='TimePicker'
                        ),
                        carbon_dash.TreeNode(
                            id='node-toggle',
                            label='Toggle',
                            value='Toggle'
                        ),
                        carbon_dash.TreeNode(
                            id='node-toggletip',
                            label='Toggletip',
                            value='Toggletip'
                        ),
                        carbon_dash.TreeNode(
                            id='node-tooltip',
                            label='Tooltip',
                            value='Tooltip'
                        ),
                        carbon_dash.TreeNode(
                            id='node-treeview',
                            label='TreeView',
                            value='TreeView'
                        ),
                        carbon_dash.TreeNode(
                            id='node-unorderedlist',
                            label='UnorderedList',
                            value='UnorderedList'
                        )
                    ]
                )
            ]
        )
    ], style={'width': '250px', 'borderRight': '1px solid #ccc', 'padding': '20px', 'height': '100vh', 'overflowY': 'auto', 'position': 'fixed'}),
    
    html.Div(
        id='main-content',
        style={'marginLeft': '290px', 'padding': '40px'}
    )
])

@app.callback(
    Output('main-content', 'children'),
    Input('component-tree', 'active')
)
def render_content(active_node):
    if active_node in stories_dict:
        return stories_dict[active_node]
    return html.Div([
        html.H2("Carbon Dash Component Gallery"),
        html.P("Select a component from the tree on the left to view its stories and API.")
    ])

if __name__ == "__main__":
    import sys
    port = 8052
    if len(sys.argv) > 1 and sys.argv[1] == "--port":
        port = int(sys.argv[2])
    app.run(debug=True, port=port)
