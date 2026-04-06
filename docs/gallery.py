import carbon_dash
import dash_iconify
from dash import Dash, html, dcc, Input, Output

app = Dash(__name__)

# Component Stories
stories_dict = {}

stories_dict['node-aiskeletonicon'] = html.Div([
        html.H2("AISkeletonIcon"),
        html.H3("_AISkeletonIcon"),
        html.Div(children=[carbon_dash.AISkeletonIcon(), carbon_dash.AISkeletonIcon()], style={'marginBottom': '20px'}),
    ])

stories_dict['node-aiskeletonplaceholder'] = html.Div([
        html.H2("AISkeletonPlaceholder"),
        html.H3("_AISkeletonPlaceholder"),
        html.Div(children=[carbon_dash.AISkeletonPlaceholder(className='test')], style={'marginBottom': '20px'}),
    ])

stories_dict['node-aiskeletontext'] = html.Div([
        html.H2("AISkeletonText"),
        html.H3("_AISkeletonText"),
        html.Div(children=[carbon_dash.AISkeletonText()], style={'marginBottom': '20px'}),
    ])

stories_dict['node-buttonset'] = html.Div([
        html.H2("ButtonSet"),
        html.H3("Controlled"),
        html.Div(children=[carbon_dash.ButtonSet(className='controlled-accordion-btnset', children=[carbon_dash.Button(className='controlled-accordion-btn', children='Click to expand all'), carbon_dash.Button(className='controlled-accordion-btn', children='Click to collapse all')]), carbon_dash.Accordion(children=[carbon_dash.AccordionItem(title='Choose your plan'), carbon_dash.AccordionItem(title='Add team members'), carbon_dash.AccordionItem(title='Set payment details'), carbon_dash.AccordionItem(title='Review and confirm')])], style={'marginBottom': '20px'}),
    ])

stories_dict['node-accordionskeleton'] = html.Div([
        html.H2("AccordionSkeleton"),
        html.H3("Skeleton"),
        html.Div(children=[carbon_dash.AccordionSkeleton(open=True, count=4)], style={'marginBottom': '20px'}),
    ])

stories_dict['node-breadcrumb'] = html.Div([
        html.H2("Breadcrumb"),
        html.H3("BreadcrumbWithOverflowMenu"),
        html.Div(children=[carbon_dash.Breadcrumb(noTrailingSlash=True, children=[carbon_dash.BreadcrumbItem(), carbon_dash.BreadcrumbItem(href='#', children='Breadcrumb 2'), carbon_dash.BreadcrumbItem(children=carbon_dash.OverflowMenu(align='bottom', children=[carbon_dash.OverflowMenuItem(itemText='Breadcrumb 3'), carbon_dash.OverflowMenuItem(itemText='Breadcrumb 4')])), carbon_dash.BreadcrumbItem(href='#', children='Breadcrumb 5'), carbon_dash.BreadcrumbItem(isCurrentPage=True, children='Breadcrumb 6')])], style={'marginBottom': '20px'}),
        html.H3("BreadcrumbWithOverflowMenuSizeSmall"),
        html.Div(children=[carbon_dash.Breadcrumb(noTrailingSlash=True, children=[carbon_dash.BreadcrumbItem(), carbon_dash.BreadcrumbItem(href='#', children='Breadcrumb 2'), carbon_dash.BreadcrumbItem(children=carbon_dash.OverflowMenu(align='bottom', children=[carbon_dash.OverflowMenuItem(itemText='Breadcrumb 3'), carbon_dash.OverflowMenuItem(itemText='Breadcrumb 4')])), carbon_dash.BreadcrumbItem(href='#', children='Breadcrumb 5'), carbon_dash.BreadcrumbItem(isCurrentPage=True, children='Breadcrumb 6')])], style={'marginBottom': '20px'}),
        html.H3("BreadcrumbWithOverflowVisualSnapshots"),
        html.Div(children=[carbon_dash.Breadcrumb(noTrailingSlash=True, children=[carbon_dash.BreadcrumbItem(), carbon_dash.BreadcrumbItem(href='#', children='Breadcrumb 2'), carbon_dash.BreadcrumbItem(children=carbon_dash.OverflowMenu(align='bottom', children=[carbon_dash.OverflowMenuItem(itemText='Breadcrumb 3'), carbon_dash.OverflowMenuItem(itemText='Breadcrumb 4')])), carbon_dash.BreadcrumbItem(href='#', children='Breadcrumb 5'), carbon_dash.BreadcrumbItem(isCurrentPage=True, children='Breadcrumb 6')])], style={'marginBottom': '20px'}),
    ])

stories_dict['node-breadcrumbskeleton'] = html.Div([
        html.H2("BreadcrumbSkeleton"),
        html.H3("Skeleton"),
        html.Div(children=[carbon_dash.BreadcrumbSkeleton()], style={'marginBottom': '20px'}),
    ])

stories_dict['node-button'] = html.Div([
        html.H2("Button"),
        html.H3("Secondary"),
        html.Div(children=[carbon_dash.Button(children='Button')], style={'marginBottom': '20px'}),
        html.H3("Tertiary"),
        html.Div(children=[carbon_dash.Button(children='Button')], style={'marginBottom': '20px'}),
        html.H3("Ghost"),
        html.Div(children=[carbon_dash.Button(children='Button')], style={'marginBottom': '20px'}),
        html.H3("Danger"),
        html.Div(children=[carbon_dash.Button(children='Button')], style={'marginBottom': '20px'}),
        html.H3("DangerTertiary"),
        html.Div(children=[carbon_dash.Button(children='Button')], style={'marginBottom': '20px'}),
        html.H3("DangerGhost"),
        html.Div(children=[carbon_dash.Button(children='Button')], style={'marginBottom': '20px'}),
        html.H3("IconButton"),
        html.Div(children=[carbon_dash.Button()], style={'marginBottom': '20px'}),
        html.H3("IconButtonWithBadge"),
        html.Div(children=[carbon_dash.Button(children='Button')], style={'marginBottom': '20px'}),
        html.H3("FullWidth"),
        html.Div(children=[carbon_dash.Button(children='Launch modal'), carbon_dash.Modal(isFullWidth=True, modalHeading='Full width modal', modalLabel='An example of a modal with no padding', primaryButtonText='Add', secondaryButtonText='Cancel', children=carbon_dash.StructuredListWrapper(style={'marginBottom': '48px'}, children=[carbon_dash.StructuredListHead(children=carbon_dash.StructuredListRow(head=True, children=[carbon_dash.StructuredListCell(head=True, noWrap=True, children='Default size'), carbon_dash.StructuredListCell(head=True, noWrap=True, children='Features'), carbon_dash.StructuredListCell(head=True, noWrap=True, children='Pricing')])), carbon_dash.StructuredListBody(children=[carbon_dash.StructuredListRow(children=[carbon_dash.StructuredListCell(noWrap=True, children='Lite'), carbon_dash.StructuredListCell(children='2 vCPUs | 4GB RAM'), carbon_dash.StructuredListCell(children='$0.12 USD / hourly')]), carbon_dash.StructuredListRow(children=[carbon_dash.StructuredListCell(noWrap=True, children='Graduated tier'), carbon_dash.StructuredListCell(children='2 vCPUs | 8GB RAM'), carbon_dash.StructuredListCell(children='$0.13 USD / hourly')]), carbon_dash.StructuredListRow(children=[carbon_dash.StructuredListCell(noWrap=True, children='Premium'), carbon_dash.StructuredListCell(children='4 vCPUs | 10GB RAM'), carbon_dash.StructuredListCell(children='$0.20 USD / hourly')])])]))], style={'marginBottom': '20px'}),
        html.H3("PassiveModal"),
        html.Div(children=[carbon_dash.Button(children='Launch modal'), carbon_dash.Modal(passiveModal=True, modalHeading='You are now signed out.')], style={'marginBottom': '20px'}),
        html.H3("WithScrollingContent"),
        html.Div(children=[carbon_dash.Button(children='Launch modal'), carbon_dash.Modal(hasScrollingContent=True, modalHeading='Add a custom domain', modalLabel='Account resources', primaryButtonText='Add', secondaryButtonText='Cancel', children=carbon_dash.MultiSelect(id='test', label='Choose options', titleText='Mapping domain', autoAlign=True, items=[{'id': 'downshift-1-item-0', 'text': 'Cloud Foundry'}, {'id': 'downshift-1-item-1', 'text': 'Kubernetes Ingress'}, {'id': 'downshift-1-item-2', 'text': 'VPC Load Balancer'}]))], style={'marginBottom': '20px'}),
        html.H3("WithInlineLoading"),
        html.Div(children=[carbon_dash.Button(children='Launch modal'), carbon_dash.Modal(danger=True, modalHeading='Are you sure you want to delete this custom domain?', modalLabel='Account resources', primaryButtonText='Delete', secondaryButtonText='Cancel')], style={'marginBottom': '20px'}),
        html.H3("Modal"),
        html.Div(children=[carbon_dash.Button(type='button', children='Toggle open')], style={'marginBottom': '20px'}),
        html.H3("NonModal"),
        html.Div(children=[carbon_dash.Button(type='button', children='Toggle open')], style={'marginBottom': '20px'}),
        html.H3("PassiveDialog"),
        html.Div(children=[carbon_dash.Button(type='button', children='Toggle open')], style={'marginBottom': '20px'}),
        html.H3("DangerDialog"),
        html.Div(children=[carbon_dash.Button(children='Toggle open')], style={'marginBottom': '20px'}),
        html.H3("DangerModal"),
        html.Div(children=[carbon_dash.Button(children='Launch modal'), carbon_dash.Modal(danger=True, modalHeading='Are you sure you want to delete this custom domain?', modalLabel='Account resources', primaryButtonText='Delete', secondaryButtonText='Cancel')], style={'marginBottom': '20px'}),
        html.H3("Dismissable"),
        html.Div(children=[carbon_dash.Button(style={'marginBottom': '3rem'}, children='Reset'), carbon_dash.Tabs(dismissable=True, children=[carbon_dash.TabList(), carbon_dash.TabPanels()])], style={'marginBottom': '20px'}),
        html.H3("DismissableContained"),
        html.Div(children=[carbon_dash.Button(style={'marginBottom': '3rem'}, children='Reset'), carbon_dash.Tabs(dismissable=True, children=[carbon_dash.TabList(contained=True), carbon_dash.TabPanels()])], style={'marginBottom': '20px'}),
        html.H3("DismissableWithIcons"),
        html.Div(children=[carbon_dash.Button(style={'marginBottom': '3rem'}, children='Reset'), carbon_dash.Tabs(dismissable=True, children=[carbon_dash.TabList(), carbon_dash.TabPanels()])], style={'marginBottom': '20px'}),
        html.H3("Dismissible"),
        html.Div(children=[carbon_dash.Button(style={'marginBottom': '3rem'}, children='Reset')], style={'marginBottom': '20px'}),
    ])

stories_dict['node-buttonskeleton'] = html.Div([
        html.H2("ButtonSkeleton"),
        html.H3("Skeleton"),
        html.Div(children=[carbon_dash.ButtonSkeleton()], style={'marginBottom': '20px'}),
    ])

stories_dict['node-checkboxgroup'] = html.Div([
        html.H2("CheckboxGroup"),
        html.H3("Horizontal"),
        html.Div(children=[carbon_dash.CheckboxGroup(orientation='horizontal', className='some-class', legendText='Group label', helperText='Helper text goes here', children=[carbon_dash.Checkbox(id='checkbox-label-1'), carbon_dash.Checkbox(id='checkbox-label-2'), carbon_dash.Checkbox(id='checkbox-label-3')])], style={'marginBottom': '20px'}),
    ])

stories_dict['node-checkbox'] = html.Div([
        html.H2("Checkbox"),
        html.H3("Single"),
        html.Div(children=[carbon_dash.Checkbox(id='checkbox-3', helperText='Helper text goes here'), carbon_dash.Checkbox(id='checkbox-4', invalid=True, invalidText='Invalid text goes here'), carbon_dash.Checkbox(id='checkbox-5', warn=True, warnText='Warning text goes here'), carbon_dash.Checkbox(id='checkbox-6', readOnly=True)], style={'marginBottom': '20px'}),
    ])

stories_dict['node-checkboxskeleton'] = html.Div([
        html.H2("CheckboxSkeleton"),
        html.H3("Skeleton"),
        html.Div(children=[carbon_dash.CheckboxSkeleton()], style={'marginBottom': '20px'}),
    ])

stories_dict['node-codesnippet'] = html.Div([
        html.H2("CodeSnippet"),
        html.H3("Inline"),
        html.Div(children=[carbon_dash.CodeSnippet(type='inline', feedback='Copied to clipboard', children='node -v')], style={'marginBottom': '20px'}),
        html.H3("Multiline"),
        html.Div(children=[carbon_dash.CodeSnippet(type='multi', feedback='Copied to clipboard', children='"scripts": {\n    "build": "lerna run build --stream --prefix --npm-client yarn",\n    "ci-check": "carbon-cli ci-check",\n    "clean": "lerna run clean && lerna clean --yes && rimraf node_modules",\n    "doctoc": "doctoc --title \'## Table of Contents\'",\n    "format": "prettier --write \'**/*.{js,md,scss,ts}\' \'!**/{build,es,lib,storybook,ts,umd}/**\'",\n    "format:diff": "\n    prettier --list-different \'**/*.{js,md,scss,ts}\' \'!**/{build,es,lib,storybook,ts,umd}/**\' \'!packages/components/**\'",\n    "lint": "eslint actions config codemods packages",\n    "lint:styles": "stylelint \'**/*.{css,scss}\' --report-needless-disables --report-invalid-scope-disables",\n    "test": "cross-env BABEL_ENV=test jest",\n    "test:e2e": "cross-env BABEL_ENV=test jest --testPathPattern=e2e --testPathIgnorePatterns=\'examples,/packages/components/,/packages/react/\'"\n  },\n  "resolutions": {\n    "react": "~16.9.0",\n    "react-dom": "~16.9.0",\n    "react-is": "~16.9.0",\n    "react-test-renderer": "~16.9.0"\n  },\n  "devDependencies": {\n    "@babel/core": "^7.10.0",\n    "@babel/plugin-proposal-class-properties": "^7.7.4",\n    "@babel/plugin-proposal-export-default-from": "^7.7.4",\n    "@babel/plugin-proposal-export-namespace-from": "^7.7.4",\n    "@babel/plugin-transform-runtime": "^7.10.0",\n    "@babel/preset-env": "^7.10.0",\n    "@babel/preset-react": "^7.10.0",\n    "@babel/runtime": "^7.10.0",\n    "@commitlint/cli": "^8.3.5",')], style={'marginBottom': '20px'}),
        html.H3("Singleline"),
        html.Div(children=[carbon_dash.CodeSnippet(type='single', feedback='Copied to clipboard', children='yarn add carbon-components@latest carbon-components-react@latest\n      @carbon/icons-react@latest carbon-icons@latest')], style={'marginBottom': '20px'}),
    ])

stories_dict['node-combobutton'] = html.Div([
        html.H2("ComboButton"),
        html.H3("FloatingStyles"),
        html.Div(children=[carbon_dash.ComboButton(label='Primary action', children=[carbon_dash.MenuItem(label='Second action with a long label description'), carbon_dash.MenuItem(label='Third action'), carbon_dash.MenuItem(label='Fourth action', disabled=True)])], style={'marginBottom': '20px'}),
        html.H3("WithDanger"),
        html.Div(children=[carbon_dash.ComboButton(label='Primary action', children=[carbon_dash.MenuItem(label='Second action with a long label description'), carbon_dash.MenuItem(label='Third action'), carbon_dash.MenuItem(label='Fourth action'), carbon_dash.MenuItemDivider(), carbon_dash.MenuItem(label='Danger action', kind='danger')])], style={'marginBottom': '20px'}),
        html.H3("WithIcons"),
        html.Div(children=[carbon_dash.ComboButton(label='Save record', children=[carbon_dash.MenuItem(label='Save as a copy', renderIcon=dash_iconify.DashIconify(icon="carbon:copy-file")), carbon_dash.MenuItem(label='Export', renderIcon=dash_iconify.DashIconify(icon="carbon:export"))])], style={'marginBottom': '20px'}),
    ])

stories_dict['node-featureflags'] = html.Div([
        html.H2("FeatureFlags"),
        html.H3("EnableDialogElement"),
        html.Div(children=[carbon_dash.FeatureFlags(enableDialogElement=True)], style={'marginBottom': '20px'}),
        html.H3("EnableFocusWrapWithoutSentinels"),
        html.Div(children=[carbon_dash.FeatureFlags(enableFocusWrapWithoutSentinels=True)], style={'marginBottom': '20px'}),
        html.H3("EnablePresence"),
        html.Div(children=[carbon_dash.FeatureFlags(enablePresence=True)], style={'marginBottom': '20px'}),
        html.H3("Nested"),
        html.Div(children=[carbon_dash.FeatureFlags(flags={'enable-v12-overflowmenu': True, 'enable-v12-dynamic-floating-styles': False}, children=carbon_dash.OverflowMenu(children=[carbon_dash.MenuItem(label='Level 1'), carbon_dash.MenuItem(label='Level 1'), carbon_dash.MenuItem(label='Level 1', children=[carbon_dash.MenuItem(label='Level 2', children=[carbon_dash.MenuItem(label='Level 3'), carbon_dash.MenuItem(label='Level 3', children=carbon_dash.MenuItem(label='Level 4'))]), carbon_dash.MenuItem(label='Level 2'), carbon_dash.MenuItem(label='Level 2')]), carbon_dash.MenuItem(label='Level 1')]))], style={'marginBottom': '20px'}),
    ])

stories_dict['node-containedlist'] = html.Div([
        html.H2("ContainedList"),
        html.H3("Disclosed"),
        html.Div(children=[carbon_dash.ContainedList(label='List title', kind='disclosed', children=[carbon_dash.ContainedListItem(children='List item'), carbon_dash.ContainedListItem(children='List item'), carbon_dash.ContainedListItem(children='List item'), carbon_dash.ContainedListItem(children='List item')]), carbon_dash.ContainedList(label='List title', kind='disclosed', children=[carbon_dash.ContainedListItem(children='List item'), carbon_dash.ContainedListItem(children='List item'), carbon_dash.ContainedListItem(children='List item'), carbon_dash.ContainedListItem(children='List item')])], style={'marginBottom': '20px'}),
        html.H3("WithInteractiveItems"),
        html.Div(children=[carbon_dash.ContainedList(label='List title', kind='on-page', children=[carbon_dash.ContainedListItem(children='List item'), carbon_dash.ContainedListItem(disabled=True, children='List item'), carbon_dash.ContainedListItem(children='List item'), carbon_dash.ContainedListItem(children='List item')])], style={'marginBottom': '20px'}),
        html.H3("WithActions"),
        html.Div(children=[carbon_dash.ContainedList(label='List title', kind='on-page', action='', children=[carbon_dash.ContainedListItem(children='List item'), carbon_dash.ContainedListItem(disabled=True, children='List item'), carbon_dash.ContainedListItem(children='List item'), carbon_dash.ContainedListItem(children='List item')])], style={'marginBottom': '20px'}),
        html.H3("WithExpandableSearch"),
        html.Div(children=[carbon_dash.ContainedList(label='List title', kind='on-page')], style={'marginBottom': '20px'}),
        html.H3("WithPersistentSearch"),
        html.Div(children=[carbon_dash.ContainedList(label='List title', kind='on-page', action='', children=carbon_dash.Search(placeholder='Filter', closeButtonLabelText='Clear search input', size='lg', labelText='Filter search'))], style={'marginBottom': '20px'}),
        html.H3("WithInteractiveItemsAndActions"),
        html.Div(children=[carbon_dash.ContainedList(label='List title', kind='on-page', action='', children=[carbon_dash.ContainedListItem(children='List item'), carbon_dash.ContainedListItem(children='List item'), carbon_dash.ContainedListItem(children='List item'), carbon_dash.ContainedListItem(children='List item')])], style={'marginBottom': '20px'}),
        html.H3("WithListTitleDecorators"),
        html.Div(children=[carbon_dash.ContainedList(kind='on-page', children=[carbon_dash.ContainedListItem(children='List item'), carbon_dash.ContainedListItem(children='List item'), carbon_dash.ContainedListItem(children='List item'), carbon_dash.ContainedListItem(children='List item')])], style={'marginBottom': '20px'}),
        html.H3("WithIcons"),
        html.Div(children=[carbon_dash.ContainedList(label='List title', kind='on-page', children=[carbon_dash.ContainedListItem(renderIcon=dash_iconify.DashIconify(icon="carbon:apple"), children='List item'), carbon_dash.ContainedListItem(renderIcon=dash_iconify.DashIconify(icon="carbon:wheat"), children='List item'), carbon_dash.ContainedListItem(renderIcon=dash_iconify.DashIconify(icon="carbon:strawberry"), children='List item'), carbon_dash.ContainedListItem(renderIcon=dash_iconify.DashIconify(icon="carbon:fish"), children='List item')])], style={'marginBottom': '20px'}),
        html.H3("UsageExamples"),
        html.Div(children=[carbon_dash.ContainedList(label='List title'), carbon_dash.ContainedList(label='List title'), carbon_dash.ContainedList(label='List title')], style={'marginBottom': '20px'}),
    ])

stories_dict['node-contentswitcher'] = html.Div([
        html.H2("ContentSwitcher"),
        html.H3("IconOnly"),
        html.Div(children=[carbon_dash.ContentSwitcher(children=[carbon_dash.IconSwitch(name='one', text='Table of Contents', children=dash_iconify.DashIconify(icon="carbon:table-of-contents")), carbon_dash.IconSwitch(name='two', text='Workspace Test', children=dash_iconify.DashIconify(icon="carbon:workspace")), carbon_dash.IconSwitch(name='three', text='View Mode', children=dash_iconify.DashIconify(icon="carbon:view-mode_2"))])], style={'marginBottom': '20px'}),
        html.H3("lowContrast"),
        html.Div(children=[carbon_dash.ContentSwitcher(lowContrast=True, children=[carbon_dash.Switch(name='one', text='First section'), carbon_dash.Switch(name='two', text='Second section'), carbon_dash.Switch(name='three', text='Third section')])], style={'marginBottom': '20px'}),
        html.H3("lowContrastIconOnly"),
        html.Div(children=[carbon_dash.ContentSwitcher(lowContrast=True, children=[carbon_dash.IconSwitch(name='one', text='Table of Contents', children=dash_iconify.DashIconify(icon="carbon:table-of-contents")), carbon_dash.IconSwitch(name='two', text='Workspace Test', children=dash_iconify.DashIconify(icon="carbon:workspace")), carbon_dash.IconSwitch(name='three', text='View Mode', children=dash_iconify.DashIconify(icon="carbon:view-mode_2"))])], style={'marginBottom': '20px'}),
    ])

stories_dict['node-menu'] = html.Div([
        html.H2("Menu"),
        html.H3("_useContextMenu"),
        html.Div(children=[carbon_dash.Menu(children=[carbon_dash.MenuItem(label='Share with', children=carbon_dash.MenuItemRadioGroup(label='Share with', items=['None', 'Product team', 'Organization', 'Company'], defaultSelectedItem='Product team')), carbon_dash.MenuItemDivider(), carbon_dash.MenuItem(label='Cut', shortcut='⌘X'), carbon_dash.MenuItem(label='Copy', shortcut='⌘C'), carbon_dash.MenuItem(label='Copy path', shortcut='⌥⌘C'), carbon_dash.MenuItem(label='Paste', disabled=True, shortcut='⌘V'), carbon_dash.MenuItem(label='Duplicate'), carbon_dash.MenuItemDivider(), carbon_dash.MenuItem(label='Rename'), carbon_dash.MenuItem(label='Delete', shortcut='⌫', kind='danger')])], style={'marginBottom': '20px'}),
        html.H3("SpecificElement"),
        html.Div(children=[carbon_dash.Menu(children=[carbon_dash.MenuItem(label='Edit'), carbon_dash.MenuItem(label='Delete', kind='danger')])], style={'marginBottom': '20px'}),
    ])

stories_dict['node-datatable'] = html.Div([
        html.H2("DataTable"),
        html.H3("AILabelWithSelection"),
        html.Div(children=[carbon_dash.DataTable(rows=[{'id': 'a', 'name': 'Load Balancer 3', 'status': 'Disabled'}, {'id': 'b', 'name': 'Load Balancer 1', 'status': 'Starting'}], headers=[{'key': 'name', 'header': 'Name'}, {'key': 'status', 'header': 'Status'}])], style={'marginBottom': '20px'}),
        html.H3("AILabelWithRadioSelection"),
        html.Div(children=[carbon_dash.DataTable(radio=True, rows=[{'id': 'a', 'name': 'Load Balancer 3', 'status': 'Disabled'}, {'id': 'b', 'name': 'Load Balancer 1', 'status': 'Starting'}], headers=[{'key': 'name', 'header': 'Name'}, {'key': 'status', 'header': 'Status'}])], style={'marginBottom': '20px'}),
        html.H3("AILabelWithSelectionAndExpansion"),
        html.Div(children=[carbon_dash.DataTable(rows=[{'id': 'a', 'name': 'Load Balancer 3', 'status': 'Disabled'}, {'id': 'b', 'name': 'Load Balancer 1', 'status': 'Starting'}], headers=[{'key': 'name', 'header': 'Name'}, {'key': 'status', 'header': 'Status'}])], style={'marginBottom': '20px'}),
        html.H3("AILabelWithExpansion"),
        html.Div(children=[carbon_dash.DataTable(rows=[{'id': 'a', 'name': 'Load Balancer 3', 'status': 'Disabled'}, {'id': 'b', 'name': 'Load Balancer 1', 'status': 'Starting'}], headers=[{'key': 'name', 'header': 'Name'}, {'key': 'status', 'header': 'Status'}])], style={'marginBottom': '20px'}),
        html.H3("ColumnAILabelWithSelectionAndExpansion"),
        html.Div(children=[carbon_dash.DataTable(headers=[{'key': 'name', 'header': 'Name'}, {'key': 'protocol', 'header': 'Protocol'}, {'key': 'port', 'header': 'Port'}, {'key': 'rule', 'header': 'Rule'}, {'key': 'attached_groups', 'header': 'Attached groups'}, {'key': 'status', 'header': 'Status'}], rows=[{'id': 'a', 'name': 'Load Balancer 3', 'status': 'Disabled'}, {'id': 'b', 'name': 'Load Balancer 1', 'status': 'Starting'}])], style={'marginBottom': '20px'}),
        html.H3("ColumnAILabelSort"),
        html.Div(children=[carbon_dash.DataTable(headers=[{'key': 'name', 'header': 'Name'}, {'key': 'protocol', 'header': 'Protocol'}, {'key': 'port', 'header': 'Port'}, {'key': 'rule', 'header': 'Rule'}, {'key': 'attached_groups', 'header': 'Attached groups'}, {'key': 'status', 'header': 'Status'}], rows=[{'id': 'a', 'name': 'Load Balancer 3', 'status': 'Disabled'}, {'id': 'b', 'name': 'Load Balancer 1', 'status': 'Starting'}])], style={'marginBottom': '20px'}),
        html.H3("FullTableAI"),
        html.Div(children=[carbon_dash.DataTable(rows=[{'id': 'a', 'name': 'Load Balancer 3', 'status': 'Disabled'}, {'id': 'b', 'name': 'Load Balancer 1', 'status': 'Starting'}], headers=[{'key': 'name', 'header': 'Name'}, {'key': 'status', 'header': 'Status'}])], style={'marginBottom': '20px'}),
        html.H3("WithRadioSelection"),
        html.Div(children=[carbon_dash.DataTable(radio=True, rows=[{'id': 'a', 'name': 'Load Balancer 3', 'status': 'Disabled'}, {'id': 'b', 'name': 'Load Balancer 1', 'status': 'Starting'}], headers=[{'key': 'name', 'header': 'Name'}, {'key': 'status', 'header': 'Status'}])], style={'marginBottom': '20px'}),
        html.H3("WithSelectionAndSorting"),
        html.Div(children=[carbon_dash.DataTable(isSortable=True, rows=[{'id': 'a', 'name': 'Load Balancer 3', 'status': 'Disabled'}, {'id': 'b', 'name': 'Load Balancer 1', 'status': 'Starting'}], headers=[{'key': 'name', 'header': 'Name'}, {'key': 'status', 'header': 'Status'}])], style={'marginBottom': '20px'}),
        html.H3("PersistentToolbar"),
        html.Div(children=[carbon_dash.DataTable(rows=[{'id': 'a', 'name': 'Load Balancer 3', 'status': 'Disabled'}, {'id': 'b', 'name': 'Load Balancer 1', 'status': 'Starting'}], headers=[{'key': 'name', 'header': 'Name'}, {'key': 'status', 'header': 'Status'}])], style={'marginBottom': '20px'}),
        html.H3("SmallPersistentToolbar"),
        html.Div(children=[carbon_dash.DataTable(rows=[{'id': 'a', 'name': 'Load Balancer 3', 'status': 'Disabled'}, {'id': 'b', 'name': 'Load Balancer 1', 'status': 'Starting'}], headers=[{'key': 'name', 'header': 'Name'}, {'key': 'status', 'header': 'Status'}])], style={'marginBottom': '20px'}),
        html.H3("WithOverflowMenu"),
        html.Div(children=[carbon_dash.DataTable(rows=[{'id': 'a', 'name': 'Load Balancer 3', 'status': 'Disabled'}, {'id': 'b', 'name': 'Load Balancer 1', 'status': 'Starting'}], headers=[{'key': 'name', 'header': 'Name'}, {'key': 'status', 'header': 'Status'}])], style={'marginBottom': '20px'}),
        html.H3("BatchExpansion"),
        html.Div(children=[carbon_dash.DataTable(rows=[{'id': 'a', 'name': 'Load Balancer 3', 'status': 'Disabled'}, {'id': 'b', 'name': 'Load Balancer 1', 'status': 'Starting'}], headers=[{'key': 'name', 'header': 'Name'}, {'key': 'status', 'header': 'Status'}])], style={'marginBottom': '20px'}),
        html.H3("BatchExpansionMultipleTables"),
        html.Div(children=[carbon_dash.DataTable(rows=[{'id': 'a', 'name': 'Load Balancer 3', 'status': 'Disabled'}, {'id': 'b', 'name': 'Load Balancer 1', 'status': 'Starting'}], headers=[{'key': 'name', 'header': 'Name'}, {'key': 'status', 'header': 'Status'}]), carbon_dash.DataTable(rows=[{'id': 'a', 'name': 'Load Balancer 3', 'status': 'Disabled'}, {'id': 'b', 'name': 'Load Balancer 1', 'status': 'Starting'}], headers=[{'key': 'name', 'header': 'Name'}, {'key': 'status', 'header': 'Status'}])], style={'marginBottom': '20px'}),
    ])

stories_dict['node-table'] = html.Div([
        html.H2("Table"),
        html.H3("XLWithTwoLines"),
        html.Div(children=[carbon_dash.Table(children=[carbon_dash.TableHead(children=carbon_dash.TableRow()), carbon_dash.TableBody()])], style={'marginBottom': '20px'}),
    ])

stories_dict['node-datepicker'] = html.Div([
        html.H2("DatePicker"),
        html.H3("Simple"),
        html.Div(children=[carbon_dash.DatePicker(datePickerType='simple', children=carbon_dash.DatePickerInput(placeholder='mm/dd/yyyy', labelText='Date Picker label', id='date-picker-simple'))], style={'marginBottom': '20px'}),
        html.H3("SingleWithCalendar"),
        html.Div(children=[carbon_dash.DatePicker(datePickerType='single', children=carbon_dash.DatePickerInput(placeholder='mm/dd/yyyy', labelText='Date Picker label', id='date-picker-single', size='md'))], style={'marginBottom': '20px'}),
        html.H3("RangeWithCalendar"),
        html.Div(children=[carbon_dash.DatePicker(datePickerType='range', children=[carbon_dash.DatePickerInput(id='date-picker-input-id-start', placeholder='mm/dd/yyyy', labelText='Start date', size='md'), carbon_dash.DatePickerInput(id='date-picker-input-id-finish', placeholder='mm/dd/yyyy', labelText='End date', size='md')])], style={'marginBottom': '20px'}),
    ])

stories_dict['node-datepickerskeleton'] = html.Div([
        html.H2("DatePickerSkeleton"),
        html.H3("Skeleton"),
        html.Div(children=[carbon_dash.DatePickerSkeleton(range=True)], style={'marginBottom': '20px'}),
    ])

stories_dict['node-fileuploaderitem'] = html.Div([
        html.H2("FileUploaderItem"),
        html.H3("_FileUploaderItem"),
        html.Div(children=[carbon_dash.FileUploaderItem(errorBody='1 MB max file size. Select a new file and try again.', errorSubject='File size exceeds limit', iconDescription='Delete file', invalid=False, name='THIS IS A VERY LONG FILENAME WHICH WILL BE TRUNCATED', status='edit', size='md')], style={'marginBottom': '20px'}),
    ])

stories_dict['node-fileuploaderdropcontainer'] = html.Div([
        html.H2("FileUploaderDropContainer"),
        html.H3("_FileUploaderDropContainer"),
        html.Div(children=[carbon_dash.FileUploaderDropContainer(labelText='Drag and drop files here or click to upload', multiple=True, accept=['image/jpeg', 'image/png'], disabled=False, name='')], style={'marginBottom': '20px'}),
    ])

stories_dict['node-fluidtextarea'] = html.Div([
        html.H2("FluidTextArea"),
        html.H3("DefaultWithToggletip"),
        html.Div(children=[carbon_dash.FluidTextArea(placeholder='Placeholder text')], style={'marginBottom': '20px'}),
    ])

stories_dict['node-fluidtextinput'] = html.Div([
        html.H2("FluidTextInput"),
        html.H3("DefaultWithToggletip"),
        html.Div(children=[carbon_dash.FluidTextInput(placeholder='Placeholder text')], style={'marginBottom': '20px'}),
    ])

stories_dict['node-stack'] = html.Div([
        html.H2("Stack"),
        html.H3("withAILabel"),
        html.Div(children=[carbon_dash.Stack(gap=7, className='form-example', children=[carbon_dash.Form(className='ai-label-form', children=carbon_dash.Stack(gap=7, children=[carbon_dash.NumberInput(), carbon_dash.DatePicker(datePickerType='single', children=carbon_dash.DatePickerInput(placeholder='mm/dd/yyyy', labelText='Date Picker label', size='md', id='date-picker')), carbon_dash.TextInput(), carbon_dash.TextArea(), carbon_dash.Dropdown(id='default', titleText='Dropdown title', helperText='This is some helper text', label='Option 1', items=[{'id': 'option-0', 'text': 'Lorem, ipsum dolor sit amet consectetur adipisicing elit.'}, {'id': 'option-1', 'text': 'Option 1'}, {'id': 'option-2', 'text': 'Option 2'}, {'id': 'option-3', 'text': 'Option 3 - a disabled item', 'disabled': True}, {'id': 'option-4', 'text': 'Option 4'}, {'id': 'option-5', 'text': 'Option 5'}]), carbon_dash.MultiSelect(label='Multiselect Label', id='carbon-multiselect-example', titleText='Multiselect title', helperText='This is helper text', items=[{'id': 'option-0', 'text': 'Lorem, ipsum dolor sit amet consectetur adipisicing elit.'}, {'id': 'option-1', 'text': 'Option 1'}, {'id': 'option-2', 'text': 'Option 2'}, {'id': 'option-3', 'text': 'Option 3 - a disabled item', 'disabled': True}, {'id': 'option-4', 'text': 'Option 4'}, {'id': 'option-5', 'text': 'Option 5'}], selectionFeedback='top-after-reopen'), carbon_dash.FilterableMultiSelect(id='carbon-multiselect-example-3', titleText='FilterableMultiselect title', items=[{'id': 'option-0', 'text': 'Lorem, ipsum dolor sit amet consectetur adipisicing elit.'}, {'id': 'option-1', 'text': 'Option 1'}, {'id': 'option-2', 'text': 'Option 2'}, {'id': 'option-3', 'text': 'Option 3 - a disabled item', 'disabled': True}, {'id': 'option-4', 'text': 'Option 4'}, {'id': 'option-5', 'text': 'Option 5'}], selectionFeedback='top-after-reopen'), carbon_dash.ComboBox(id='carbon-combobox', items=[{'id': 'option-0', 'text': 'Lorem, ipsum dolor sit amet consectetur adipisicing elit.'}, {'id': 'option-1', 'text': 'Option 1'}, {'id': 'option-2', 'text': 'Option 2'}, {'id': 'option-3', 'text': 'Option 3 - a disabled item', 'disabled': True}, {'id': 'option-4', 'text': 'Option 4'}, {'id': 'option-5', 'text': 'Option 5'}], titleText='ComboBox title', helperText='Combobox helper text'), carbon_dash.Select(id='select-1', labelText='Select an option', helperText='Optional helper text', children=[carbon_dash.SelectItem(value='', text=''), carbon_dash.SelectItem(value='An example option that is really long to show what should be done to handle long text', text='An example option that is really long to show what should be done to handle long text'), carbon_dash.SelectItem(value='Option 2', text='Option 2'), carbon_dash.SelectItem(value='Option 3', text='Option 3'), carbon_dash.SelectItem(value='Option 4', text='Option 4')]), carbon_dash.Button(type='submit', className='some-class', children='Submit')])), carbon_dash.FluidForm(className='fluid-ai-label-form', children=carbon_dash.Button(type='submit', className='some-class', children='Submit'))])], style={'marginBottom': '20px'}),
        html.H3("Horizontal"),
        html.Div(children=[carbon_dash.Stack(gap=6, orientation='horizontal')], style={'marginBottom': '20px'}),
    ])

stories_dict['node-actionablenotification'] = html.Div([
        html.H2("ActionableNotification"),
        html.H3("WithToggletip"),
        html.Div(children=[carbon_dash.ActionableNotification(kind='info', hideCloseButton=True, lowContrast=True, inline=True, className='notification', actionButtonLabel='Accessibility button note on form labels', title='Accessibility note')], style={'marginBottom': '20px'}),
        html.H3("FocusWrapWithoutSentinels"),
        html.Div(children=[carbon_dash.ActionableNotification()], style={'marginBottom': '20px'}),
    ])

stories_dict['node-heading'] = html.Div([
        html.H2("Heading"),
        html.H3("CustomLevel"),
        html.Div(children=[carbon_dash.Heading(children='h1'), carbon_dash.Section(level=5, children=[carbon_dash.Heading(children='h5'), carbon_dash.Section(children=carbon_dash.Heading(children='h6'))])], style={'marginBottom': '20px'}),
        html.H3("UsageExamples"),
        html.Div(children=[carbon_dash.Heading(), carbon_dash.Button(kind='ghost'), carbon_dash.ContentSwitcher(children=[carbon_dash.Switch(name='one'), carbon_dash.Switch(name='two', text='Second section'), carbon_dash.Switch(name='three', text='Third section')])], style={'marginBottom': '20px'}),
    ])

stories_dict['node-icons'] = html.Div([
        html.H2("Icons"),
        html.H3("WithRelativeSize"),
        html.Div(children=[dash_iconify.DashIconify(icon="carbon:edit")], style={'marginBottom': '20px'}),
    ])

stories_dict['node-layer'] = html.Div([
        html.H2("Layer"),
        html.H3("withBackground"),
        html.Div(children=[carbon_dash.Layer(withBackground=True, children=carbon_dash.Layer(withBackground=True))], style={'marginBottom': '20px'}),
        html.H3("CustomLevel"),
        html.Div(children=[carbon_dash.Layer(level=2)], style={'marginBottom': '20px'}),
        html.H3("UseLayer"),
        html.Div(children=[carbon_dash.Layer()], style={'marginBottom': '20px'}),
    ])

stories_dict['node-link'] = html.Div([
        html.H2("Link"),
        html.H3("Inline"),
        html.Div(children=[carbon_dash.Link(children='Lorem ipsum dolor sit amet, consectetur adipiscing elit.')], style={'marginBottom': '20px'}),
        html.H3("PairedWithIcon"),
        html.Div(children=[carbon_dash.Link(href='#', children='Carbon Docs')], style={'marginBottom': '20px'}),
    ])

stories_dict['node-menubutton'] = html.Div([
        html.H2("MenuButton"),
        html.H3("FloatingStyles"),
        html.Div(children=[carbon_dash.MenuButton(label='Actions', children=[carbon_dash.MenuItem(label='First action'), carbon_dash.MenuItem(label='Second action that is a longer item to test overflow and title.'), carbon_dash.MenuItem(label='Third action', disabled=True)])], style={'marginBottom': '20px'}),
        html.H3("WithDanger"),
        html.Div(children=[carbon_dash.MenuButton(label='Actions', children=[carbon_dash.MenuItem(label='First action'), carbon_dash.MenuItem(label='Second action'), carbon_dash.MenuItem(label='Third action'), carbon_dash.MenuItemDivider(), carbon_dash.MenuItem(label='Danger action', kind='danger')])], style={'marginBottom': '20px'}),
        html.H3("WithDividers"),
        html.Div(children=[carbon_dash.MenuButton(label='Actions', children=[carbon_dash.MenuItem(label='Create service request'), carbon_dash.MenuItem(label='Create work order'), carbon_dash.MenuItemDivider(), carbon_dash.MenuItem(label='Add plan'), carbon_dash.MenuItem(label='Add flag'), carbon_dash.MenuItemDivider(), carbon_dash.MenuItem(label='Edit source location'), carbon_dash.MenuItem(label='Recalculate source')])], style={'marginBottom': '20px'}),
        html.H3("WithIcons"),
        html.Div(children=[carbon_dash.MenuButton(label='Add', children=[carbon_dash.MenuItem(label='Asset', renderIcon=dash_iconify.DashIconify(icon="carbon:asset")), carbon_dash.MenuItem(label='User', renderIcon=dash_iconify.DashIconify(icon="carbon:user")), carbon_dash.MenuItem(label='User group', renderIcon=dash_iconify.DashIconify(icon="carbon:group"))])], style={'marginBottom': '20px'}),
        html.H3("WithNestedMenu"),
        html.Div(children=[carbon_dash.MenuButton(label='Actions', children=[carbon_dash.MenuItem(label='Save', shortcut='⌘S'), carbon_dash.MenuItem(label='Save as', shortcut='⌥⌘S'), carbon_dash.MenuItem(label='Export as', children=[carbon_dash.MenuItem(label='PDF'), carbon_dash.MenuItem(label='JPG'), carbon_dash.MenuItem(label='PNG')]), carbon_dash.MenuItemDivider(), carbon_dash.MenuItem(label='Delete', kind='danger')])], style={'marginBottom': '20px'}),
    ])

stories_dict['node-multiselect'] = html.Div([
        html.H2("MultiSelect"),
        html.H3("FloatingStyles"),
        html.Div(children=[carbon_dash.MultiSelect(id='carbon-multiselect-example', items=[{'id': 'option-0', 'text': 'An example option that is really long to show what should be done to handle long text'}, {'id': 'option-1', 'text': 'Option 1'}, {'id': 'option-2', 'text': 'Option 2'}, {'id': 'option-3', 'text': 'Option 3 - a disabled item', 'disabled': True}, {'id': 'option-4', 'text': 'Option 4'}, {'id': 'option-5', 'text': 'Option 5'}], selectionFeedback='top-after-reopen')], style={'marginBottom': '20px'}),
    ])

stories_dict['node-callout'] = html.Div([
        html.H2("Callout"),
        html.H3("WithInteractiveElements"),
        html.Div(children=[carbon_dash.Callout(title='Notification title', titleId='my fancy id 123', kind='info', lowContrast=True)], style={'marginBottom': '20px'}),
    ])

stories_dict['node-numberinput'] = html.Div([
        html.H2("NumberInput"),
        html.H3("WithTypeOfText"),
        html.Div(children=[carbon_dash.NumberInput(id='default-number-input', inputMode='decimal', defaultValue=50, label='NumberInput label', helperText='Optional helper text.')], style={'marginBottom': '20px'}),
        html.H3("WithTypeOfTextControlled"),
        html.Div(children=[carbon_dash.NumberInput(id='default-number-input', type='text', inputMode='decimal', label='NumberInput label', helperText='Optional helper text.')], style={'marginBottom': '20px'}),
        html.H3("WithTypeOfCustomValidation"),
        html.Div(children=[carbon_dash.NumberInput(id='default-number-input', type='text', inputMode='decimal', label='NumberInput label', helperText='Optional helper text.', allowEmpty=True)], style={'marginBottom': '20px'}),
    ])

stories_dict['node-numberinputskeleton'] = html.Div([
        html.H2("NumberInputSkeleton"),
        html.H3("Skeleton"),
        html.Div(children=[carbon_dash.NumberInputSkeleton()], style={'marginBottom': '20px'}),
    ])

stories_dict['node-orderedlist'] = html.Div([
        html.H2("OrderedList"),
        html.H3("Nested"),
        html.Div(children=[carbon_dash.OrderedList(children=[carbon_dash.ListItem(children=['Ordered List level 1', carbon_dash.OrderedList(nested=True, children=[carbon_dash.ListItem(children='Ordered List level 2'), carbon_dash.ListItem(children=['Ordered List level 2', carbon_dash.OrderedList(nested=True, children=[carbon_dash.ListItem(children='Ordered List level 3'), carbon_dash.ListItem(children='Ordered List level 3')])])])]), carbon_dash.ListItem(children='Ordered List level 1'), carbon_dash.ListItem(children='Ordered List level 1')])], style={'marginBottom': '20px'}),
        html.H3("NativeListStyles"),
        html.Div(children=[carbon_dash.OrderedList(native=True, children=[carbon_dash.ListItem(children='Ordered List level 1'), carbon_dash.ListItem(children='Ordered List level 1'), carbon_dash.ListItem(children='Ordered List level 1'), carbon_dash.ListItem(children=['Ordered List level 1', carbon_dash.OrderedList(nested=True, children=[carbon_dash.ListItem(children='Ordered List level 2'), carbon_dash.ListItem(children='Ordered List level 2'), carbon_dash.ListItem(children='Ordered List level 2'), carbon_dash.ListItem(children='Ordered List level 2')])]), carbon_dash.ListItem(children='Ordered List level 1'), carbon_dash.ListItem(children='Ordered List level 1'), carbon_dash.ListItem(children='Ordered List level 1'), carbon_dash.ListItem(children='Ordered List level 1'), carbon_dash.ListItem(children='Ordered List level 1'), carbon_dash.ListItem(children='Ordered List level 1'), carbon_dash.ListItem(children='Ordered List level 1'), carbon_dash.ListItem(children='Ordered List level 1')])], style={'marginBottom': '20px'}),
    ])

stories_dict['node-overflowmenu'] = html.Div([
        html.H2("OverflowMenu"),
        html.H3("RenderCustomIcon"),
        html.Div(children=[carbon_dash.OverflowMenu(renderIcon=dash_iconify.DashIconify(icon="carbon:filter"), children=[carbon_dash.OverflowMenuItem(itemText='Filter A'), carbon_dash.OverflowMenuItem(itemText='Filter B')])], style={'marginBottom': '20px'}),
    ])

stories_dict['node-tabs'] = html.Div([
        html.H2("Tabs"),
        html.H3("TabBarWithTabsAndTags"),
        html.Div(children=[carbon_dash.Tabs(children=carbon_dash.TabPanels(children=[carbon_dash.TabPanel(children='Tab Panel 1'), carbon_dash.TabPanel(children='Tab Panel 2'), carbon_dash.TabPanel(children='Tab Panel 3'), carbon_dash.TabPanel(children='Tab Panel 4'), carbon_dash.TabPanel(children='Tab Panel 5'), carbon_dash.TabPanel(children='Tab Panel 6'), carbon_dash.TabPanel(children='Tab Panel 7')]))], style={'marginBottom': '20px'}),
        html.H3("WithIcons"),
        html.Div(children=[carbon_dash.Tabs(children=[carbon_dash.TabList(activation='manual', children=[carbon_dash.Tab(renderIcon=dash_iconify.DashIconify(icon="carbon:dashboard"), children='Dashboard'), carbon_dash.Tab(renderIcon=dash_iconify.DashIconify(icon="carbon:cloud-monitoring"), children='Monitoring'), carbon_dash.Tab(renderIcon=dash_iconify.DashIconify(icon="carbon:activity"), children='Activity'), carbon_dash.Tab(renderIcon=dash_iconify.DashIconify(icon="carbon:ibm-watson-discovery"), children='Analyze'), carbon_dash.Tab(disabled=True, renderIcon=dash_iconify.DashIconify(icon="carbon:settings"), children='Settings')]), carbon_dash.TabPanels(children=[carbon_dash.TabPanel(children='Tab Panel 1'), carbon_dash.TabPanel(), carbon_dash.TabPanel(children='Tab Panel 3'), carbon_dash.TabPanel(children='Tab Panel 4'), carbon_dash.TabPanel(children='Tab Panel 5')])])], style={'marginBottom': '20px'}),
        html.H3("Manual"),
        html.Div(children=[carbon_dash.Tabs(children=[carbon_dash.TabList(activation='manual', children=[carbon_dash.Tab(children='Dashboard'), carbon_dash.Tab(children='Monitoring'), carbon_dash.Tab(children='Activity'), carbon_dash.Tab(children='Analyze'), carbon_dash.Tab(disabled=True, children='Settings')]), carbon_dash.TabPanels(children=[carbon_dash.TabPanel(children='Tab Panel 1'), carbon_dash.TabPanel(), carbon_dash.TabPanel(children='Tab Panel 3'), carbon_dash.TabPanel(children='Tab Panel 4'), carbon_dash.TabPanel(children='Tab Panel 5')])])], style={'marginBottom': '20px'}),
        html.H3("Icon20Only"),
        html.Div(children=[carbon_dash.Tabs(children=[carbon_dash.TabList(iconSize='lg', children=[carbon_dash.IconTab(label='Analyze', children=dash_iconify.DashIconify(icon="carbon:ibm-watson-discovery")), carbon_dash.IconTab(label='Activity', children=dash_iconify.DashIconify(icon="carbon:activity")), carbon_dash.IconTab(label='New Notifications', children=dash_iconify.DashIconify(icon="carbon:notification")), carbon_dash.IconTab(label='Chat', children=dash_iconify.DashIconify(icon="carbon:chat"))]), carbon_dash.TabPanels(children=[carbon_dash.TabPanel(children='Tab Panel 1'), carbon_dash.TabPanel(children='Tab Panel 2'), carbon_dash.TabPanel(children='Tab Panel 3'), carbon_dash.TabPanel(children='Tab Panel 4')])])], style={'marginBottom': '20px'}),
        html.H3("IconOnly"),
        html.Div(children=[carbon_dash.Tabs(children=[carbon_dash.TabList(iconSize='default', children=[carbon_dash.IconTab(label='Analyze', children=dash_iconify.DashIconify(icon="carbon:ibm-watson-discovery")), carbon_dash.IconTab(label='Activity', children=dash_iconify.DashIconify(icon="carbon:activity")), carbon_dash.IconTab(label='New Notifications', children=dash_iconify.DashIconify(icon="carbon:notification")), carbon_dash.IconTab(label='Chat', children=dash_iconify.DashIconify(icon="carbon:chat"))]), carbon_dash.TabPanels(children=[carbon_dash.TabPanel(children='Tab Panel 1'), carbon_dash.TabPanel(children='Tab Panel 2'), carbon_dash.TabPanel(children='Tab Panel 3'), carbon_dash.TabPanel(children='Tab Panel 4')])])], style={'marginBottom': '20px'}),
        html.H3("Contained"),
        html.Div(children=[carbon_dash.Tabs(children=[carbon_dash.TabList(contained=True, children=[carbon_dash.Tab(children='Dashboard'), carbon_dash.Tab(children='Monitoring'), carbon_dash.Tab(children='Activity'), carbon_dash.Tab(children='Analyze'), carbon_dash.Tab(disabled=True, children='Settings')]), carbon_dash.TabPanels(children=[carbon_dash.TabPanel(children='Tab Panel 1'), carbon_dash.TabPanel(children=carbon_dash.Layer()), carbon_dash.TabPanel(children='Tab Panel 3'), carbon_dash.TabPanel(children='Tab Panel 4'), carbon_dash.TabPanel(children='Tab Panel 5')])])], style={'marginBottom': '20px'}),
        html.H3("ContainedWithIcons"),
        html.Div(children=[carbon_dash.Tabs(children=[carbon_dash.TabList(contained=True, children=[carbon_dash.Tab(renderIcon=dash_iconify.DashIconify(icon="carbon:dashboard"), children='Dashboard'), carbon_dash.Tab(renderIcon=dash_iconify.DashIconify(icon="carbon:cloud-monitoring"), children='Monitoring'), carbon_dash.Tab(renderIcon=dash_iconify.DashIconify(icon="carbon:activity"), children='Activity'), carbon_dash.Tab(renderIcon=dash_iconify.DashIconify(icon="carbon:ibm-watson-discovery"), children='Analyze'), carbon_dash.Tab(disabled=True, renderIcon=dash_iconify.DashIconify(icon="carbon:settings"), children='Settings')]), carbon_dash.TabPanels(children=[carbon_dash.TabPanel(children='Tab Panel 1'), carbon_dash.TabPanel(children=carbon_dash.Layer()), carbon_dash.TabPanel(children='Tab Panel 3'), carbon_dash.TabPanel(children='Tab Panel 4'), carbon_dash.TabPanel(children='Tab Panel 5')])])], style={'marginBottom': '20px'}),
        html.H3("ContainedWithSecondaryLabels"),
        html.Div(children=[carbon_dash.Tabs(children=[carbon_dash.TabList(contained=True, children=[carbon_dash.Tab(secondaryLabel='(21/25)', children='Engage'), carbon_dash.Tab(secondaryLabel='(12/16)', children='Analyze'), carbon_dash.Tab(secondaryLabel='(0/7)', children='Remediate'), carbon_dash.Tab(secondaryLabel='(4/12)', children='Assets'), carbon_dash.Tab(disabled=True, secondaryLabel='(0/10)', children='Monitoring')]), carbon_dash.TabPanels(children=[carbon_dash.TabPanel(children='Tab Panel 1'), carbon_dash.TabPanel(children=carbon_dash.Layer()), carbon_dash.TabPanel(children='Tab Panel 3'), carbon_dash.TabPanel(children='Tab Panel 4'), carbon_dash.TabPanel(children='Tab Panel 5')])])], style={'marginBottom': '20px'}),
        html.H3("ContainedWithSecondaryLabelsAndIcons"),
        html.Div(children=[carbon_dash.Tabs(children=[carbon_dash.TabList(contained=True, children=[carbon_dash.Tab(renderIcon=dash_iconify.DashIconify(icon="carbon:task"), secondaryLabel='(21/25', children='Engage'), carbon_dash.Tab(renderIcon=dash_iconify.DashIconify(icon="carbon:ibm-watson-discovery"), secondaryLabel='(12/16)', children='Analyze'), carbon_dash.Tab(renderIcon=dash_iconify.DashIconify(icon="carbon:restart"), disabled=True, secondaryLabel='(0/7)', children='Remediate'), carbon_dash.Tab(renderIcon=dash_iconify.DashIconify(icon="carbon:dashboard"), secondaryLabel='(4/12)', children='Assets'), carbon_dash.Tab(renderIcon=dash_iconify.DashIconify(icon="carbon:cloud-monitoring"), secondaryLabel='(1/23)', children='Monitoring')]), carbon_dash.TabPanels(children=[carbon_dash.TabPanel(children='Tab Panel 1'), carbon_dash.TabPanel(children=carbon_dash.Layer()), carbon_dash.TabPanel(children='Tab Panel 3'), carbon_dash.TabPanel(children='Tab Panel 4'), carbon_dash.TabPanel(children='Tab Panel 5')])])], style={'marginBottom': '20px'}),
        html.H3("Icon20OnlyVisualSnapshots"),
        html.Div(children=[carbon_dash.Tabs(children=[carbon_dash.TabList(iconSize='lg', children=[carbon_dash.IconTab(label='Analyze', children=dash_iconify.DashIconify(icon="carbon:ibm-watson-discovery")), carbon_dash.IconTab(label='Activity', children=dash_iconify.DashIconify(icon="carbon:activity")), carbon_dash.IconTab(label='New Notifications', children=dash_iconify.DashIconify(icon="carbon:notification")), carbon_dash.IconTab(label='Chat', children=dash_iconify.DashIconify(icon="carbon:chat"))]), carbon_dash.TabPanels(children=[carbon_dash.TabPanel(children='Tab Panel 1'), carbon_dash.TabPanel(children='Tab Panel 2'), carbon_dash.TabPanel(children='Tab Panel 3'), carbon_dash.TabPanel(children='Tab Panel 4')])])], style={'marginBottom': '20px'}),
        html.H3("IconOnlyVisualSnapshots"),
        html.Div(children=[carbon_dash.Tabs(children=[carbon_dash.TabList(iconSize='default', children=[carbon_dash.IconTab(label='Analyze', children=dash_iconify.DashIconify(icon="carbon:ibm-watson-discovery")), carbon_dash.IconTab(label='Activity', children=dash_iconify.DashIconify(icon="carbon:activity")), carbon_dash.IconTab(label='New Notifications', children=dash_iconify.DashIconify(icon="carbon:notification")), carbon_dash.IconTab(label='Chat', children=dash_iconify.DashIconify(icon="carbon:chat"))]), carbon_dash.TabPanels(children=[carbon_dash.TabPanel(children='Tab Panel 1'), carbon_dash.TabPanel(children='Tab Panel 2'), carbon_dash.TabPanel(children='Tab Panel 3'), carbon_dash.TabPanel(children='Tab Panel 4')])])], style={'marginBottom': '20px'}),
    ])

stories_dict['node-progressbar'] = html.Div([
        html.H2("ProgressBar"),
        html.H3("Indeterminate"),
        html.Div(children=[carbon_dash.ProgressBar(label='Progress bar label', helperText='Optional helper text')], style={'marginBottom': '20px'}),
        html.H3("Determinate"),
        html.Div(children=[carbon_dash.ProgressBar(label='Export data')], style={'marginBottom': '20px'}),
    ])

stories_dict['node-progressindicator'] = html.Div([
        html.H2("ProgressIndicator"),
        html.H3("Interactive"),
        html.Div(children=[carbon_dash.ProgressIndicator(currentIndex=1, children=[carbon_dash.ProgressStep(label='Click me', description='Step 1: Register an onChange event'), carbon_dash.ProgressStep(label='Really long label', description='The progress indicator will listen for clicks on the steps'), carbon_dash.ProgressStep(label='Third step', description='The progress indicator will listen for clicks on the steps')])], style={'marginBottom': '20px'}),
    ])

stories_dict['node-progressindicatorskeleton'] = html.Div([
        html.H2("ProgressIndicatorSkeleton"),
        html.H3("Skeleton"),
        html.Div(children=[carbon_dash.ProgressIndicatorSkeleton()], style={'marginBottom': '20px'}),
    ])

stories_dict['node-radiobuttongroup'] = html.Div([
        html.H2("RadioButtonGroup"),
        html.H3("Vertical"),
        html.Div(children=[carbon_dash.RadioButtonGroup(legendText='Group label', name='radio-button-vertical-group', defaultSelected='radio-1', orientation='vertical', children=[carbon_dash.RadioButton(labelText='Radio button label', value='radio-1', id='radio-1'), carbon_dash.RadioButton(labelText='Radio button label', value='radio-2', id='radio-2'), carbon_dash.RadioButton(labelText='Radio button label', value='radio-3', id='radio-3', disabled=True)])], style={'marginBottom': '20px'}),
    ])

stories_dict['node-radiobuttonskeleton'] = html.Div([
        html.H2("RadioButtonSkeleton"),
        html.H3("Skeleton"),
        html.Div(children=[carbon_dash.RadioButtonSkeleton()], style={'marginBottom': '20px'}),
    ])

stories_dict['node-search'] = html.Div([
        html.H2("Search"),
        html.H3("Disabled"),
        html.Div(children=[carbon_dash.Search(disabled=True, size='lg', placeholder='Find your items', labelText='Search', closeButtonLabelText='Clear search input', id='search-1')], style={'marginBottom': '20px'}),
    ])

stories_dict['node-selectskeleton'] = html.Div([
        html.H2("SelectSkeleton"),
        html.H3("Skeleton"),
        html.Div(children=[carbon_dash.SelectSkeleton()], style={'marginBottom': '20px'}),
    ])

stories_dict['node-slider'] = html.Div([
        html.H2("Slider"),
        html.H3("SliderWithHiddenInputs"),
        html.Div(children=[carbon_dash.Slider(labelText='Slider label', value=50, min=0, max=100, step=1, stepMultiplier=10, invalidText='Invalid message goes here', hideTextInput=True)], style={'marginBottom': '20px'}),
        html.H3("SliderWithCustomValueLabel"),
        html.Div(children=[carbon_dash.Slider(labelText='Slider label with low/medium/high', value=50, min=0, max=100, stepMultiplier=50, step=1, hideTextInput=True)], style={'marginBottom': '20px'}),
        html.H3("ControlledSlider"),
        html.Div(children=[carbon_dash.Slider(labelText='Slider label', max=100, min=0)], style={'marginBottom': '20px'}),
        html.H3("TwoHandleSlider"),
        html.Div(children=[carbon_dash.Slider(ariaLabelInput='Lower bound', unstable_ariaLabelInputUpper='Upper bound', labelText='Slider label', value=10, unstable_valueUpper=90, min=0, max=100, step=1, stepMultiplier=10, invalidText='Invalid message goes here')], style={'marginBottom': '20px'}),
        html.H3("TwoHandleSliderWithHiddenInputs"),
        html.Div(children=[carbon_dash.Slider(ariaLabelInput='Lower bound', unstable_ariaLabelInputUpper='Upper bound', labelText='Slider label', value=10, unstable_valueUpper=90, min=0, max=100, step=1, stepMultiplier=10, invalidText='Invalid message goes here', hideTextInput=True)], style={'marginBottom': '20px'}),
    ])

stories_dict['node-sliderskeleton'] = html.Div([
        html.H2("SliderSkeleton"),
        html.H3("Skeleton"),
        html.Div(children=[carbon_dash.SliderSkeleton()], style={'marginBottom': '20px'}),
        html.H3("TwoHandleSkeleton"),
        html.Div(children=[carbon_dash.SliderSkeleton(twoHandles=True)], style={'marginBottom': '20px'}),
    ])

stories_dict['node-structuredlistwrapper'] = html.Div([
        html.H2("StructuredListWrapper"),
        html.H3("Selection"),
        html.Div(children=[carbon_dash.StructuredListWrapper(selection=True, children=[carbon_dash.StructuredListHead(children=carbon_dash.StructuredListRow(head=True, children=[carbon_dash.StructuredListCell(head=True, children='ColumnA'), carbon_dash.StructuredListCell(head=True, children='ColumnB'), carbon_dash.StructuredListCell(head=True, children='ColumnC')])), carbon_dash.StructuredListBody()])], style={'marginBottom': '20px'}),
        html.H3("InitialSelection"),
        html.Div(children=[carbon_dash.StructuredListWrapper(selection=True, selectedInitialRow='row-2', children=[carbon_dash.StructuredListHead(children=carbon_dash.StructuredListRow(head=True, children=[carbon_dash.StructuredListCell(head=True, children='ColumnA'), carbon_dash.StructuredListCell(head=True, children='ColumnB'), carbon_dash.StructuredListCell(head=True, children='ColumnC')])), carbon_dash.StructuredListBody()])], style={'marginBottom': '20px'}),
    ])

stories_dict['node-grid'] = html.Div([
        html.H2("Grid"),
        html.H3("ContainedFullWidth"),
        html.Div(children=[carbon_dash.Grid(condensed=True, children=carbon_dash.Column(lg=16, md=8, sm=4, children=carbon_dash.Tabs(children=[carbon_dash.TabList(contained=True, fullWidth=True, children=[carbon_dash.Tab(children='TLS'), carbon_dash.Tab(children='Origin'), carbon_dash.Tab(disabled=True, children='Rate limiting'), carbon_dash.Tab(children='WAF'), carbon_dash.Tab(children='IP Firewall'), carbon_dash.Tab(children='Firewall rules'), carbon_dash.Tab(children='Range'), carbon_dash.Tab(children='Mutual TLS')]), carbon_dash.TabPanels(children=[carbon_dash.TabPanel(children='Tab Panel 1'), carbon_dash.TabPanel(children=carbon_dash.Layer()), carbon_dash.TabPanel(children='Tab Panel 3'), carbon_dash.TabPanel(children='Tab Panel 4'), carbon_dash.TabPanel(children='Tab Panel 5'), carbon_dash.TabPanel(children='Tab Panel 6'), carbon_dash.TabPanel(children='Tab Panel 7'), carbon_dash.TabPanel(children='Tab Panel 8')])])))], style={'marginBottom': '20px'}),
    ])

stories_dict['node-tabsvertical'] = html.Div([
        html.H2("TabsVertical"),
        html.H3("Vertical"),
        html.Div(children=[carbon_dash.TabsVertical(children=[carbon_dash.TabListVertical(children=[carbon_dash.Tab(children='Dashboard'), carbon_dash.Tab(children='Extra long label that will go two lines then truncate when it goes\n          beyond the Tab length'), carbon_dash.Tab(children='Activity'), carbon_dash.Tab(children='Analyze'), carbon_dash.Tab(children='Investigate'), carbon_dash.Tab(children='Learn'), carbon_dash.Tab(disabled=True, children='Settings')]), carbon_dash.TabPanels(children=[carbon_dash.TabPanel(children='Tab Panel 1'), carbon_dash.TabPanel(children=carbon_dash.Layer()), carbon_dash.TabPanel(children='Tab Panel 3'), carbon_dash.TabPanel(children='Tab Panel 4'), carbon_dash.TabPanel(children='Tab Panel 5'), carbon_dash.TabPanel(children='Tab Panel 6'), carbon_dash.TabPanel(children='Tab Panel 7')])])], style={'marginBottom': '20px'}),
    ])

stories_dict['node-tag'] = html.Div([
        html.H2("Tag"),
        html.H3("ReadOnly"),
        html.Div(children=[carbon_dash.Tag(className='some-class', type='red', children='Tag content with a long text description'), carbon_dash.Tag(className='some-class', type='magenta', children='Tag content'), carbon_dash.Tag(className='some-class', type='purple', children='Tag content'), carbon_dash.Tag(className='some-class', type='blue', children='Tag content'), carbon_dash.Tag(className='some-class', type='cyan', children='Tag content'), carbon_dash.Tag(className='some-class', type='teal', children='Tag content'), carbon_dash.Tag(className='some-class', type='green', children='Tag content'), carbon_dash.Tag(className='some-class', type='gray', children='Tag content'), carbon_dash.Tag(className='some-class', type='cool-gray', children='Tag content'), carbon_dash.Tag(className='some-class', type='warm-gray', children='Tag content'), carbon_dash.Tag(className='some-class', type='high-contrast', children='Tag content'), carbon_dash.Tag(className='some-class', type='outline', children='Tag content')], style={'marginBottom': '20px'}),
    ])

stories_dict['node-textarea'] = html.Div([
        html.H2("TextArea"),
        html.H3("withAILabel"),
        html.Div(children=[carbon_dash.TextArea(labelText='Text Area label', helperText='Optional helper text', rows=4, id='text-area-5')], style={'marginBottom': '20px'}),
    ])

stories_dict['node-textareaskeleton'] = html.Div([
        html.H2("TextAreaSkeleton"),
        html.H3("Skeleton"),
        html.Div(children=[carbon_dash.TextAreaSkeleton()], style={'marginBottom': '20px'}),
    ])

stories_dict['node-textinputskeleton'] = html.Div([
        html.H2("TextInputSkeleton"),
        html.H3("Skeleton"),
        html.Div(children=[carbon_dash.TextInputSkeleton()], style={'marginBottom': '20px'}),
    ])

stories_dict['node-theme'] = html.Div([
        html.H2("Theme"),
        html.H3("UsePrefersDarkScheme"),
        html.Div(children=[carbon_dash.Theme(children=[carbon_dash.Theme(), carbon_dash.Theme(), carbon_dash.Theme()])], style={'marginBottom': '20px'}),
    ])

stories_dict['node-vstack'] = html.Div([
        html.H2("VStack"),
        html.H3("_WithLayer"),
        html.Div(children=[carbon_dash.VStack(gap=7)], style={'marginBottom': '20px'}),
        html.H3("WithAccessibleLabels"),
        html.Div(children=[carbon_dash.VStack(gap=7, children=[carbon_dash.Toggle(id='toggle-4', labelText='Label'), carbon_dash.Toggle(id='toggle-5', labelText='Label', hideLabel=True)])], style={'marginBottom': '20px'}),
    ])

stories_dict['node-clickabletile'] = html.Div([
        html.H2("ClickableTile"),
        html.H3("Clickable"),
        html.Div(children=[carbon_dash.ClickableTile(id='clickable-tile-1', href='https://www.carbondesignsystem.com/', children='Clickable Tile')], style={'marginBottom': '20px'}),
        html.H3("ClickableWithCustomIcon"),
        html.Div(children=[carbon_dash.ClickableTile(id='clickable-tile-1', href='https://www.carbondesignsystem.com/', renderIcon=dash_iconify.DashIconify(icon="carbon:launch"), children='Clickable Tile')], style={'marginBottom': '20px'}),
    ])

stories_dict['node-selectabletile'] = html.Div([
        html.H2("SelectableTile"),
        html.H3("Selectable"),
        html.Div(children=[carbon_dash.SelectableTile(id='selectable-tile-1', children='Selectable')], style={'marginBottom': '20px'}),
    ])

stories_dict['node-tilegroup'] = html.Div([
        html.H2("TileGroup"),
        html.H3("Radio"),
        html.Div(children=[carbon_dash.TileGroup(defaultSelected='default-selected', legend='Radio Tile Group', name='radio tile group', children=[carbon_dash.RadioTile(id='radio-tile-1', value='standard', style={'marginBottom': '.5rem'}, children='Option 1'), carbon_dash.RadioTile(id='radio-tile-2', value='default-selected', style={'marginBottom': '.5rem'}, children='Option 2'), carbon_dash.RadioTile(id='radio-tile-3', value='selected', children='Option 3')])], style={'marginBottom': '20px'}),
    ])

stories_dict['node-toggle'] = html.Div([
        html.H2("Toggle"),
        html.H3("SmallToggle"),
        html.Div(children=[carbon_dash.Toggle(size='sm', labelText='Label', labelA='Off', labelB='On', defaultToggled=True, id='toggle-2')], style={'marginBottom': '20px'}),
    ])

stories_dict['node-tooltip'] = html.Div([
        html.H2("Tooltip"),
        html.H3("Alignment"),
        html.Div(children=[carbon_dash.Tooltip(label='Tooltip alignment', align='bottom-left', children=carbon_dash.Button(children='This button has a tooltip'))], style={'marginBottom': '20px'}),
        html.H3("Duration"),
        html.Div(children=[carbon_dash.Tooltip(label='Label one', enterDelayMs=0, leaveDelayMs=300, children=carbon_dash.Button(children='This button has a tooltip'))], style={'marginBottom': '20px'}),
    ])

stories_dict['node-treeview'] = html.Div([
        html.H2("TreeView"),
        html.H3("WithIcons"),
        html.Div(children=[carbon_dash.TreeView(label='Tree View')], style={'marginBottom': '20px'}),
        html.H3("WithControlledExpansion"),
        html.Div(children=[carbon_dash.TreeView(label='Tree View')], style={'marginBottom': '20px'}),
        html.H3("WithComplexNesting"),
        html.Div(children=[carbon_dash.TreeView(label='Tree View with Complex Nesting', children=[carbon_dash.TreeNode(id='1', value='A.I.', label='A.I.', isExpanded=True, children=carbon_dash.TreeNode(id='1-2', value='Sub 2', label='Sub 2 (direct child)', children=carbon_dash.TreeNode(id='1-2-1', value='Sub 2.1', label='Sub 2.1'))), carbon_dash.TreeNode(id='2', value='Analytics', label='Analytics', isExpanded=True), carbon_dash.TreeNode(id='3', value='Trust', label='Trust')])], style={'marginBottom': '20px'}),
    ])

stories_dict['node-headercontainer'] = html.Div([
        html.H2("HeaderContainer"),
        html.H3("HeaderWNavigation"),
        html.Div(children=[carbon_dash.HeaderContainer(children=carbon_dash.Header(children=[carbon_dash.SkipToContent(), carbon_dash.HeaderMenuButton(), carbon_dash.HeaderName(href='#', prefix='IBM', children='[Platform]'), carbon_dash.HeaderNavigation(children=[carbon_dash.HeaderMenuItem(children='Link 1'), carbon_dash.HeaderMenuItem(children='Link 2'), carbon_dash.HeaderMenuItem(children='Link 3'), carbon_dash.HeaderMenu(menuLinkName='Link 4', children=[carbon_dash.HeaderMenuItem(children='Sub-link 1'), carbon_dash.HeaderMenuItem(isActive=True, children='Sub-link 2'), carbon_dash.HeaderMenuItem(children='Sub-link 3')])]), carbon_dash.SideNav(isPersistent=False, children=carbon_dash.SideNavItems(children=carbon_dash.HeaderSideNavItems(children=[carbon_dash.HeaderMenuItem(children='Link 1'), carbon_dash.HeaderMenuItem(children='Link 2'), carbon_dash.HeaderMenuItem(children='Link 3'), carbon_dash.HeaderMenu(menuLinkName='Link 4', children=[carbon_dash.HeaderMenuItem(children='Sub-link 1'), carbon_dash.HeaderMenuItem(isActive=True, children='Sub-link 2'), carbon_dash.HeaderMenuItem(children='Sub-link 3')])])))]))], style={'marginBottom': '20px'}),
        html.H3("HeaderWNavigationAndActions"),
        html.Div(children=[carbon_dash.HeaderContainer(children=carbon_dash.Header(children=[carbon_dash.SkipToContent(), carbon_dash.HeaderMenuButton(), carbon_dash.HeaderName(href='#', prefix='IBM', children='[Platform]'), carbon_dash.HeaderNavigation(children=[carbon_dash.HeaderMenuItem(children='Link 1'), carbon_dash.HeaderMenuItem(children='Link 2'), carbon_dash.HeaderMenuItem(children='Link 3'), carbon_dash.HeaderMenu(isActive=True, menuLinkName='Link 4', children=[carbon_dash.HeaderMenuItem(children='Sub-link 1'), carbon_dash.HeaderMenuItem(children='Sub-link 2'), carbon_dash.HeaderMenuItem(children='Sub-link 3')])]), carbon_dash.HeaderGlobalBar(children=[carbon_dash.HeaderGlobalAction(children=carbon_dash.Search(size=20)), carbon_dash.HeaderGlobalAction(children=dash_iconify.DashIconify(icon="carbon:notification")), carbon_dash.HeaderGlobalAction(tooltipAlignment='end')]), carbon_dash.SideNav(isPersistent=False, children=carbon_dash.SideNavItems(children=carbon_dash.HeaderSideNavItems(children=[carbon_dash.HeaderMenuItem(children='Link 1'), carbon_dash.HeaderMenuItem(children='Link 2'), carbon_dash.HeaderMenuItem(children='Link 3'), carbon_dash.HeaderMenu(menuLinkName='Link 4', children=[carbon_dash.HeaderMenuItem(children='Sub-link 1'), carbon_dash.HeaderMenuItem(children='Sub-link 2'), carbon_dash.HeaderMenuItem(children='Sub-link 3')])])))]))], style={'marginBottom': '20px'}),
        html.H3("HeaderWNavigationActionsAndSideNav"),
        html.Div(children=[carbon_dash.HeaderContainer(children=carbon_dash.Header(children=[carbon_dash.SkipToContent(), carbon_dash.HeaderMenuButton(), carbon_dash.HeaderName(href='#', prefix='IBM', children='[Platform]'), carbon_dash.HeaderNavigation(children=[carbon_dash.HeaderMenuItem(children='Link 1'), carbon_dash.HeaderMenuItem(children='Link 2'), carbon_dash.HeaderMenuItem(children='Link 3'), carbon_dash.HeaderMenu(menuLinkName='Link 4', children=[carbon_dash.HeaderMenuItem(children='Sub-link 1'), carbon_dash.HeaderMenuItem(children='Sub-link 2'), carbon_dash.HeaderMenuItem(children='Sub-link 3')])]), carbon_dash.HeaderGlobalBar(children=[carbon_dash.HeaderGlobalAction(tooltipAlignment='start', children=carbon_dash.Search(size=20)), carbon_dash.HeaderGlobalAction(children=dash_iconify.DashIconify(icon="carbon:notification")), carbon_dash.HeaderGlobalAction(tooltipAlignment='end')]), carbon_dash.SideNav(href='#main-content', children=carbon_dash.SideNavItems(children=[carbon_dash.HeaderSideNavItems(hasDivider=True, children=[carbon_dash.HeaderMenuItem(children='Link 1'), carbon_dash.HeaderMenuItem(children='Link 2'), carbon_dash.HeaderMenuItem(children='Link 3'), carbon_dash.HeaderMenu(menuLinkName='Link 4', children=[carbon_dash.HeaderMenuItem(children='Sub-link 1'), carbon_dash.HeaderMenuItem(children='Sub-link 2'), carbon_dash.HeaderMenuItem(children='Sub-link 3')])]), carbon_dash.SideNavMenu(renderIcon=dash_iconify.DashIconify(icon="carbon:fade"), title='Category title', tabIndex=0, children=[carbon_dash.SideNavMenuItem(href='https://www.carbondesignsystem.com/', children='Link 5'), carbon_dash.SideNavMenuItem(href='https://www.carbondesignsystem.com/', children='Link 6'), carbon_dash.SideNavMenuItem(href='https://www.carbondesignsystem.com/', children='Link 7')]), carbon_dash.SideNavMenu(renderIcon=dash_iconify.DashIconify(icon="carbon:fade"), title='Category title', tabIndex=0, children=[carbon_dash.SideNavMenuItem(href='https://www.carbondesignsystem.com/', children='Link 8'), carbon_dash.SideNavMenuItem(href='https://www.carbondesignsystem.com/', children='Link 9'), carbon_dash.SideNavMenuItem(href='https://www.carbondesignsystem.com/', children='Link 10')]), carbon_dash.SideNavMenu(renderIcon=dash_iconify.DashIconify(icon="carbon:fade"), title='Category title', isActive=True, tabIndex=0, children=[carbon_dash.SideNavMenuItem(href='https://www.carbondesignsystem.com/', children='Link 11'), carbon_dash.SideNavMenuItem(href='https://www.carbondesignsystem.com/', children='Link 12'), carbon_dash.SideNavMenuItem(href='https://www.carbondesignsystem.com/', children='Link 13')]), carbon_dash.SideNavLink(renderIcon=dash_iconify.DashIconify(icon="carbon:fade"), children='Link'), carbon_dash.SideNavLink(renderIcon=dash_iconify.DashIconify(icon="carbon:fade"), children='Link')]))]))], style={'marginBottom': '20px'}),
        html.H3("HeaderWSideNav"),
        html.Div(children=[carbon_dash.HeaderContainer(children=carbon_dash.Header(children=[carbon_dash.SkipToContent(), carbon_dash.HeaderMenuButton(), carbon_dash.HeaderName(href='#', prefix='IBM', children='[Platform]'), carbon_dash.SideNav(href='#main-content', children=carbon_dash.SideNavItems(children=[carbon_dash.SideNavMenu(renderIcon=dash_iconify.DashIconify(icon="carbon:fade"), title='Category title', children=[carbon_dash.SideNavMenuItem(href='https://www.carbondesignsystem.com/', children='Link'), carbon_dash.SideNavMenuItem(href='https://www.carbondesignsystem.com/', children='Link'), carbon_dash.SideNavMenuItem(href='https://www.carbondesignsystem.com/', children='Link')]), carbon_dash.SideNavMenu(renderIcon=dash_iconify.DashIconify(icon="carbon:fade"), title='Category title', isActive=True, children=[carbon_dash.SideNavMenuItem(href='https://www.carbondesignsystem.com/', children='Link'), carbon_dash.SideNavMenuItem(href='https://www.carbondesignsystem.com/', children='Link'), carbon_dash.SideNavMenuItem(href='https://www.carbondesignsystem.com/', children='Link')]), carbon_dash.SideNavMenu(renderIcon=dash_iconify.DashIconify(icon="carbon:fade"), title='Category title', children=[carbon_dash.SideNavMenuItem(href='https://www.carbondesignsystem.com/', children='Link'), carbon_dash.SideNavMenuItem(href='https://www.carbondesignsystem.com/', children='Link'), carbon_dash.SideNavMenuItem(href='https://www.carbondesignsystem.com/', children='Link')]), carbon_dash.SideNavLink(renderIcon=dash_iconify.DashIconify(icon="carbon:fade"), children='Link'), carbon_dash.SideNavLink(renderIcon=dash_iconify.DashIconify(icon="carbon:fade"), children='Link')]))]))], style={'marginBottom': '20px'}),
        html.H3("HeaderWActionsAndSwitcher"),
        html.Div(children=[carbon_dash.HeaderContainer(children=carbon_dash.Header(children=[carbon_dash.HeaderName(href='#', prefix='IBM', children='[Platform]'), carbon_dash.HeaderGlobalBar(children=[carbon_dash.HeaderGlobalAction(children=carbon_dash.Search(size=20)), carbon_dash.HeaderGlobalAction(children=dash_iconify.DashIconify(icon="carbon:notification")), carbon_dash.HeaderGlobalAction(tooltipAlignment='end', id='switcher-button')]), carbon_dash.HeaderPanel(href='#switcher-button', children=carbon_dash.Switcher(children=[carbon_dash.SwitcherItem(href='#', children='Link 1'), carbon_dash.SwitcherDivider(), carbon_dash.SwitcherItem(href='#', children='Link 2'), carbon_dash.SwitcherItem(href='#', children='Link 3'), carbon_dash.SwitcherItem(href='#', children='Link 4'), carbon_dash.SwitcherItem(href='#', children='Link 5'), carbon_dash.SwitcherDivider(), carbon_dash.SwitcherItem(href='#', children='Link 6')]))]))], style={'marginBottom': '20px'}),
        html.H3("SideNavRailWHeader"),
        html.Div(children=[carbon_dash.HeaderContainer(children=carbon_dash.Header(children=[carbon_dash.SkipToContent(), carbon_dash.HeaderMenuButton(), carbon_dash.HeaderName(href='#', prefix='IBM', children='[Platform]'), carbon_dash.HeaderNavigation(children=[carbon_dash.HeaderMenuItem(children='Link 1'), carbon_dash.HeaderMenuItem(children='Link 2'), carbon_dash.HeaderMenuItem(children='Link 3'), carbon_dash.HeaderMenu(menuLinkName='Link 4', children=[carbon_dash.HeaderMenuItem(children='Sub-link 1'), carbon_dash.HeaderMenuItem(children='Sub-link 2'), carbon_dash.HeaderMenuItem(children='Sub-link 3')])]), carbon_dash.HeaderGlobalBar(children=[carbon_dash.HeaderGlobalAction(children=carbon_dash.Search(size=20)), carbon_dash.HeaderGlobalAction(children=dash_iconify.DashIconify(icon="carbon:notification")), carbon_dash.HeaderGlobalAction(tooltipAlignment='end')]), carbon_dash.SideNav(href='#main-content', isRail=True, children=carbon_dash.SideNavItems(children=[carbon_dash.SideNavMenu(renderIcon=dash_iconify.DashIconify(icon="carbon:fade"), title='Category title', children=[carbon_dash.SideNavMenuItem(href='https://www.carbondesignsystem.com/', children='Link'), carbon_dash.SideNavMenuItem(href='https://www.carbondesignsystem.com/', children='Link'), carbon_dash.SideNavMenuItem(href='https://www.carbondesignsystem.com/', children='Link')]), carbon_dash.SideNavMenu(renderIcon=dash_iconify.DashIconify(icon="carbon:fade"), title='Category title', children=[carbon_dash.SideNavMenuItem(href='https://www.carbondesignsystem.com/', children='Link'), carbon_dash.SideNavMenuItem(href='https://www.carbondesignsystem.com/', children='Link'), carbon_dash.SideNavMenuItem(href='https://www.carbondesignsystem.com/', children='Link')]), carbon_dash.SideNavMenu(renderIcon=dash_iconify.DashIconify(icon="carbon:fade"), title='Category title', children=[carbon_dash.SideNavMenuItem(href='https://www.carbondesignsystem.com/', children='Link'), carbon_dash.SideNavMenuItem(href='https://www.carbondesignsystem.com/', children='Link'), carbon_dash.SideNavMenuItem(href='https://www.carbondesignsystem.com/', children='Link')]), carbon_dash.SideNavLink(renderIcon=dash_iconify.DashIconify(icon="carbon:fade"), children='Link'), carbon_dash.SideNavLink(renderIcon=dash_iconify.DashIconify(icon="carbon:fade"), children='Link')]))]))], style={'marginBottom': '20px'}),
    ])

stories_dict['node-header'] = html.Div([
        html.H2("Header"),
        html.H3("HeaderWActionsAndRightPanel"),
        html.Div(children=[carbon_dash.Header(children=[carbon_dash.HeaderName(href='#', prefix='IBM', children='[Platform]'), carbon_dash.HeaderGlobalBar(children=[carbon_dash.HeaderGlobalAction(children=carbon_dash.Search(size=20)), carbon_dash.HeaderGlobalAction(tooltipAlignment='center', id='notification-button', children=dash_iconify.DashIconify(icon="carbon:notification")), carbon_dash.HeaderGlobalAction(tooltipAlignment='end')]), carbon_dash.HeaderPanel(href='#notification-button')])], style={'marginBottom': '20px'}),
        html.H3("FixedSideNav"),
        html.Div(children=[carbon_dash.Header(children=[carbon_dash.SkipToContent(), carbon_dash.HeaderName(href='#', prefix='IBM', children='[Platform]')]), carbon_dash.SideNav(isFixedNav=True, expanded=True, isChildOfHeader=False, children=carbon_dash.SideNavItems(children=[carbon_dash.SideNavMenu(title='L0 menu', children=[carbon_dash.SideNavMenuItem(href='https://www.carbondesignsystem.com/', children='L0 menu item'), carbon_dash.SideNavMenuItem(href='https://www.carbondesignsystem.com/', children='L0 menu item'), carbon_dash.SideNavMenuItem(href='https://www.carbondesignsystem.com/', children='L0 menu item')]), carbon_dash.SideNavMenu(title='L0 menu', isActive=True, children=[carbon_dash.SideNavMenuItem(href='https://www.carbondesignsystem.com/', children='L0 menu item'), carbon_dash.SideNavMenuItem(href='https://www.carbondesignsystem.com/', children='L0 menu item'), carbon_dash.SideNavMenuItem(href='https://www.carbondesignsystem.com/', children='L0 menu item')]), carbon_dash.SideNavMenu(title='L0 menu', children=[carbon_dash.SideNavMenuItem(href='https://www.carbondesignsystem.com/', children='L0 menu item'), carbon_dash.SideNavMenuItem(href='https://www.carbondesignsystem.com/', children='L0 menu item'), carbon_dash.SideNavMenuItem(href='https://www.carbondesignsystem.com/', children='L0 menu item')]), carbon_dash.SideNavLink(children='L0 link'), carbon_dash.SideNavLink(children='L0 link')]))], style={'marginBottom': '20px'}),
        html.H3("FixedSideNavWIcons"),
        html.Div(children=[carbon_dash.Header(children=[carbon_dash.SkipToContent(), carbon_dash.HeaderName(href='#', prefix='IBM', children='[Platform]')]), carbon_dash.SideNav(isFixedNav=True, expanded=True, isChildOfHeader=False, children=carbon_dash.SideNavItems(children=[carbon_dash.SideNavMenu(renderIcon=dash_iconify.DashIconify(icon="carbon:fade"), title='Category title', children=[carbon_dash.SideNavMenuItem(href='https://www.carbondesignsystem.com/', children='Link'), carbon_dash.SideNavMenuItem(href='https://www.carbondesignsystem.com/', children='Link'), carbon_dash.SideNavMenuItem(href='https://www.carbondesignsystem.com/', children='Link')]), carbon_dash.SideNavMenu(renderIcon=dash_iconify.DashIconify(icon="carbon:fade"), title='Category title', isActive=True, children=[carbon_dash.SideNavMenuItem(href='https://www.carbondesignsystem.com/', children='Link'), carbon_dash.SideNavMenuItem(href='https://www.carbondesignsystem.com/', children='Link'), carbon_dash.SideNavMenuItem(href='https://www.carbondesignsystem.com/', children='Link')]), carbon_dash.SideNavMenu(renderIcon=dash_iconify.DashIconify(icon="carbon:fade"), title='Category title', children=[carbon_dash.SideNavMenuItem(href='https://www.carbondesignsystem.com/', children='Link'), carbon_dash.SideNavMenuItem(href='https://www.carbondesignsystem.com/', children='Link'), carbon_dash.SideNavMenuItem(href='https://www.carbondesignsystem.com/', children='Link')]), carbon_dash.SideNavLink(renderIcon=dash_iconify.DashIconify(icon="carbon:fade"), children='Link'), carbon_dash.SideNavLink(renderIcon=dash_iconify.DashIconify(icon="carbon:fade"), children='Link')]))], style={'marginBottom': '20px'}),
        html.H3("FixedSideNavWDivider"),
        html.Div(children=[carbon_dash.Header(children=[carbon_dash.SkipToContent(), carbon_dash.HeaderName(href='#', prefix='IBM', children='[Platform]')]), carbon_dash.SideNav(isFixedNav=True, expanded=True, isChildOfHeader=False, children=carbon_dash.SideNavItems(children=[carbon_dash.SideNavMenu(title='L0 menu', children=[carbon_dash.SideNavMenuItem(href='https://www.carbondesignsystem.com/', children='L0 menu item'), carbon_dash.SideNavMenuItem(href='https://www.carbondesignsystem.com/', children='L0 menu item'), carbon_dash.SideNavMenuItem(href='https://www.carbondesignsystem.com/', children='L0 menu item')]), carbon_dash.SideNavMenu(title='L0 menu', isActive=True, children=[carbon_dash.SideNavMenuItem(href='https://www.carbondesignsystem.com/', children='L0 menu item'), carbon_dash.SideNavMenuItem(href='https://www.carbondesignsystem.com/', children='L0 menu item'), carbon_dash.SideNavMenuItem(href='https://www.carbondesignsystem.com/', children='L0 menu item')]), carbon_dash.SideNavMenu(title='L0 menu', children=[carbon_dash.SideNavMenuItem(href='https://www.carbondesignsystem.com/', children='L0 menu item'), carbon_dash.SideNavMenuItem(href='https://www.carbondesignsystem.com/', children='L0 menu item'), carbon_dash.SideNavMenuItem(href='https://www.carbondesignsystem.com/', children='L0 menu item')]), carbon_dash.SideNavDivider(), carbon_dash.SideNavLink(children='L0 link'), carbon_dash.SideNavLink(children='L0 link')]))], style={'marginBottom': '20px'}),
        html.H3("SideNavWLargeSideNavItems"),
        html.Div(children=[carbon_dash.Header(children=[carbon_dash.SkipToContent(), carbon_dash.HeaderName(href='#', prefix='IBM', children='[Platform]')]), carbon_dash.SideNav(expanded=True, isChildOfHeader=False, children=carbon_dash.SideNavItems(children=[carbon_dash.SideNavMenu(title='Large menu', large=True, children=[carbon_dash.SideNavMenuItem(href='https://www.carbondesignsystem.com/', children='Menu 1'), carbon_dash.SideNavMenuItem(href='https://www.carbondesignsystem.com/', children='Menu 2'), carbon_dash.SideNavMenuItem(href='https://www.carbondesignsystem.com/', children='Menu 3')]), carbon_dash.SideNavLink(large=True, children='Large link'), carbon_dash.SideNavMenu(renderIcon=dash_iconify.DashIconify(icon="carbon:fade"), title='Large menu w/icon', large=True, children=[carbon_dash.SideNavMenuItem(href='https://www.carbondesignsystem.com/', children='Menu 1'), carbon_dash.SideNavMenuItem(href='https://www.carbondesignsystem.com/', children='Menu 2'), carbon_dash.SideNavMenuItem(href='https://www.carbondesignsystem.com/', children='Menu 3')]), carbon_dash.SideNavLink(renderIcon=dash_iconify.DashIconify(icon="carbon:fade"), large=True, children='Large link w/icon')]))], style={'marginBottom': '20px'}),
    ])

stories_dict['node-unorderedlist'] = html.Div([
        html.H2("UnorderedList"),
        html.H3("Nested"),
        html.Div(children=[carbon_dash.UnorderedList(children=[carbon_dash.ListItem(children=['Unordered List level 1', carbon_dash.UnorderedList(nested=True, children=[carbon_dash.ListItem(children='Unordered List level 2'), carbon_dash.ListItem(children=['Unordered List level 2', carbon_dash.UnorderedList(nested=True, children=[carbon_dash.ListItem(children='Unordered List level 2'), carbon_dash.ListItem(children='Unordered List level 2')])])])]), carbon_dash.ListItem(children='Unordered List level 1'), carbon_dash.ListItem(children='Unordered List level 1')])], style={'marginBottom': '20px'}),
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
                            id='node-accordionskeleton',
                            label='AccordionSkeleton',
                            value='AccordionSkeleton'
                        ),
                        carbon_dash.TreeNode(
                            id='node-actionablenotification',
                            label='ActionableNotification',
                            value='ActionableNotification'
                        ),
                        carbon_dash.TreeNode(
                            id='node-aiskeletonicon',
                            label='AISkeletonIcon',
                            value='AISkeletonIcon'
                        ),
                        carbon_dash.TreeNode(
                            id='node-aiskeletonplaceholder',
                            label='AISkeletonPlaceholder',
                            value='AISkeletonPlaceholder'
                        ),
                        carbon_dash.TreeNode(
                            id='node-aiskeletontext',
                            label='AISkeletonText',
                            value='AISkeletonText'
                        ),
                        carbon_dash.TreeNode(
                            id='node-breadcrumb',
                            label='Breadcrumb',
                            value='Breadcrumb'
                        ),
                        carbon_dash.TreeNode(
                            id='node-breadcrumbskeleton',
                            label='BreadcrumbSkeleton',
                            value='BreadcrumbSkeleton'
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
                            id='node-buttonskeleton',
                            label='ButtonSkeleton',
                            value='ButtonSkeleton'
                        ),
                        carbon_dash.TreeNode(
                            id='node-callout',
                            label='Callout',
                            value='Callout'
                        ),
                        carbon_dash.TreeNode(
                            id='node-checkbox',
                            label='Checkbox',
                            value='Checkbox'
                        ),
                        carbon_dash.TreeNode(
                            id='node-checkboxgroup',
                            label='CheckboxGroup',
                            value='CheckboxGroup'
                        ),
                        carbon_dash.TreeNode(
                            id='node-checkboxskeleton',
                            label='CheckboxSkeleton',
                            value='CheckboxSkeleton'
                        ),
                        carbon_dash.TreeNode(
                            id='node-clickabletile',
                            label='ClickableTile',
                            value='ClickableTile'
                        ),
                        carbon_dash.TreeNode(
                            id='node-codesnippet',
                            label='CodeSnippet',
                            value='CodeSnippet'
                        ),
                        carbon_dash.TreeNode(
                            id='node-combobutton',
                            label='ComboButton',
                            value='ComboButton'
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
                            id='node-datepicker',
                            label='DatePicker',
                            value='DatePicker'
                        ),
                        carbon_dash.TreeNode(
                            id='node-datepickerskeleton',
                            label='DatePickerSkeleton',
                            value='DatePickerSkeleton'
                        ),
                        carbon_dash.TreeNode(
                            id='node-featureflags',
                            label='FeatureFlags',
                            value='FeatureFlags'
                        ),
                        carbon_dash.TreeNode(
                            id='node-fileuploaderdropcontainer',
                            label='FileUploaderDropContainer',
                            value='FileUploaderDropContainer'
                        ),
                        carbon_dash.TreeNode(
                            id='node-fileuploaderitem',
                            label='FileUploaderItem',
                            value='FileUploaderItem'
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
                            id='node-grid',
                            label='Grid',
                            value='Grid'
                        ),
                        carbon_dash.TreeNode(
                            id='node-header',
                            label='Header',
                            value='Header'
                        ),
                        carbon_dash.TreeNode(
                            id='node-headercontainer',
                            label='HeaderContainer',
                            value='HeaderContainer'
                        ),
                        carbon_dash.TreeNode(
                            id='node-heading',
                            label='Heading',
                            value='Heading'
                        ),
                        carbon_dash.TreeNode(
                            id='node-icons',
                            label='Icons',
                            value='Icons'
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
                            id='node-menu',
                            label='Menu',
                            value='Menu'
                        ),
                        carbon_dash.TreeNode(
                            id='node-menubutton',
                            label='MenuButton',
                            value='MenuButton'
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
                            id='node-numberinputskeleton',
                            label='NumberInputSkeleton',
                            value='NumberInputSkeleton'
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
                            id='node-progressindicatorskeleton',
                            label='ProgressIndicatorSkeleton',
                            value='ProgressIndicatorSkeleton'
                        ),
                        carbon_dash.TreeNode(
                            id='node-radiobuttongroup',
                            label='RadioButtonGroup',
                            value='RadioButtonGroup'
                        ),
                        carbon_dash.TreeNode(
                            id='node-radiobuttonskeleton',
                            label='RadioButtonSkeleton',
                            value='RadioButtonSkeleton'
                        ),
                        carbon_dash.TreeNode(
                            id='node-search',
                            label='Search',
                            value='Search'
                        ),
                        carbon_dash.TreeNode(
                            id='node-selectabletile',
                            label='SelectableTile',
                            value='SelectableTile'
                        ),
                        carbon_dash.TreeNode(
                            id='node-selectskeleton',
                            label='SelectSkeleton',
                            value='SelectSkeleton'
                        ),
                        carbon_dash.TreeNode(
                            id='node-slider',
                            label='Slider',
                            value='Slider'
                        ),
                        carbon_dash.TreeNode(
                            id='node-sliderskeleton',
                            label='SliderSkeleton',
                            value='SliderSkeleton'
                        ),
                        carbon_dash.TreeNode(
                            id='node-stack',
                            label='Stack',
                            value='Stack'
                        ),
                        carbon_dash.TreeNode(
                            id='node-structuredlistwrapper',
                            label='StructuredListWrapper',
                            value='StructuredListWrapper'
                        ),
                        carbon_dash.TreeNode(
                            id='node-table',
                            label='Table',
                            value='Table'
                        ),
                        carbon_dash.TreeNode(
                            id='node-tabs',
                            label='Tabs',
                            value='Tabs'
                        ),
                        carbon_dash.TreeNode(
                            id='node-tabsvertical',
                            label='TabsVertical',
                            value='TabsVertical'
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
                            id='node-textareaskeleton',
                            label='TextAreaSkeleton',
                            value='TextAreaSkeleton'
                        ),
                        carbon_dash.TreeNode(
                            id='node-textinputskeleton',
                            label='TextInputSkeleton',
                            value='TextInputSkeleton'
                        ),
                        carbon_dash.TreeNode(
                            id='node-theme',
                            label='Theme',
                            value='Theme'
                        ),
                        carbon_dash.TreeNode(
                            id='node-tilegroup',
                            label='TileGroup',
                            value='TileGroup'
                        ),
                        carbon_dash.TreeNode(
                            id='node-toggle',
                            label='Toggle',
                            value='Toggle'
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
                        ),
                        carbon_dash.TreeNode(
                            id='node-vstack',
                            label='VStack',
                            value='VStack'
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
