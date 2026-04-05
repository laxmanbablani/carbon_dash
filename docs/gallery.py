import carbon_dash
import dash_iconify
from dash import Dash, html, dcc, Input, Output

app = Dash(__name__)

# Component Stories
stories_dict = {}

stories_dict['node-ailabel'] = html.Div([
        html.H2("AILabel"),
        html.H3("Default"),
        carbon_dash.AILabel(id='ailabel-default'),
        html.H3("Inline"),
        carbon_dash.AILabel(kind='inline', id='ailabel-inline'),
        html.H3("InlineWithContent"),
        carbon_dash.AILabel(kind='inline', textLabel='Text goes here', id='ailabel-inlinewithcontent'),
    ])

stories_dict['node-accordion'] = html.Div([
        html.H2("Accordion"),
        html.H3("Default"),
        carbon_dash.Accordion(id='accordion-default'),
        html.H3("Controlled"),
        carbon_dash.Accordion(id='accordion-controlled'),
        html.H3("_WithLayer"),
        carbon_dash.Accordion(id='accordion-_withlayer'),
        html.H3("Skeleton"),
        carbon_dash.AccordionSkeleton(open=True, count=4, align='end', isFlush=False, ordered=False),
    ])

stories_dict['node-breadcrumb'] = html.Div([
        html.H2("Breadcrumb"),
        html.H3("BreadcrumbWithOverflowMenu"),
        carbon_dash.Breadcrumb(noTrailingSlash=True, children=[carbon_dash.BreadcrumbItem(), carbon_dash.BreadcrumbItem(href='#', children='Breadcrumb 2'), carbon_dash.BreadcrumbItem(children=carbon_dash.OverflowMenu(align='bottom', children=[carbon_dash.OverflowMenuItem(itemText='Breadcrumb 3'), carbon_dash.OverflowMenuItem(itemText='Breadcrumb 4')])), carbon_dash.BreadcrumbItem(href='#', children='Breadcrumb 5'), carbon_dash.BreadcrumbItem(isCurrentPage=True, children='Breadcrumb 6')]),
        html.H3("BreadcrumbWithOverflowMenuSizeSmall"),
        carbon_dash.Breadcrumb(noTrailingSlash=True, children=[carbon_dash.BreadcrumbItem(), carbon_dash.BreadcrumbItem(href='#', children='Breadcrumb 2'), carbon_dash.BreadcrumbItem(children=carbon_dash.OverflowMenu(align='bottom', children=[carbon_dash.OverflowMenuItem(itemText='Breadcrumb 3'), carbon_dash.OverflowMenuItem(itemText='Breadcrumb 4')])), carbon_dash.BreadcrumbItem(href='#', children='Breadcrumb 5'), carbon_dash.BreadcrumbItem(isCurrentPage=True, children='Breadcrumb 6')], size='sm'),
        html.H3("Skeleton"),
        carbon_dash.BreadcrumbSkeleton(items=3),
        html.H3("BreadcrumbWithOverflowVisualSnapshots"),
        carbon_dash.Breadcrumb(noTrailingSlash=True, children=[carbon_dash.BreadcrumbItem(), carbon_dash.BreadcrumbItem(href='#', children='Breadcrumb 2'), carbon_dash.BreadcrumbItem(children=carbon_dash.OverflowMenu(align='bottom', children=[carbon_dash.OverflowMenuItem(itemText='Breadcrumb 3'), carbon_dash.OverflowMenuItem(itemText='Breadcrumb 4')])), carbon_dash.BreadcrumbItem(href='#', children='Breadcrumb 5'), carbon_dash.BreadcrumbItem(isCurrentPage=True, children='Breadcrumb 6')]),
    ])

stories_dict['node-button'] = html.Div([
        html.H2("Button"),
        html.H3("Secondary"),
        carbon_dash.Button(children='Button', kind='secondary'),
        html.H3("Tertiary"),
        carbon_dash.Button(children='Button', kind='tertiary'),
        html.H3("Ghost"),
        carbon_dash.Button(children='Button', kind='ghost'),
        html.H3("Danger"),
        carbon_dash.Button(children='Button', kind='danger'),
        html.H3("DangerTertiary"),
        carbon_dash.Button(children='Button', kind='danger--tertiary'),
        html.H3("DangerGhost"),
        carbon_dash.Button(children='Button', kind='danger--ghost'),
        html.H3("IconButton"),
        carbon_dash.Button(hasIconOnly=True, renderIcon='Add', iconDescription='Icon Description'),
        html.H3("IconButtonWithBadge"),
        carbon_dash.Button(children='Button', hasIconOnly=True, renderIcon='Notification', iconDescription='Notification', kind='ghost', size='lg'),
        html.H3("Skeleton"),
        carbon_dash.ButtonSkeleton(),
    ])

stories_dict['node-buttonset'] = html.Div([
        html.H2("ButtonSet"),
        html.H3("Fluid"),
        carbon_dash.ButtonSet(fluid=True, id='buttonset-fluid'),
    ])

stories_dict['node-checkbox'] = html.Div([
        html.H2("Checkbox"),
        html.H3("Default"),
        carbon_dash.Checkbox(id='checkbox-default'),
        html.H3("Horizontal"),
        carbon_dash.CheckboxGroup(orientation='horizontal', className='some-class', legendText='Group label', helperText='Helper text goes here', children=[carbon_dash.Checkbox(id='checkbox-label-1'), carbon_dash.Checkbox(id='checkbox-label-2'), carbon_dash.Checkbox(id='checkbox-label-3')]),
        html.H3("Single"),
        carbon_dash.Checkbox(id='checkbox-single'),
        html.H3("Skeleton"),
        carbon_dash.CheckboxSkeleton(),
        html.H3("withAILabel"),
        carbon_dash.Checkbox(invalid=False, invalidText='Invalid message goes here', readOnly=False, warn=False, warnText='Warning message goes here', id='checkbox-withailabel'),
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
        carbon_dash.CodeSnippet(id='codesnippet-inlinewithlayer'),
        html.H3("MultilineWithLayer"),
        carbon_dash.CodeSnippet(id='codesnippet-multilinewithlayer'),
        html.H3("SinglelineWithLayer"),
        carbon_dash.CodeSnippet(id='codesnippet-singlelinewithlayer'),
        html.H3("Skeleton"),
        carbon_dash.CodeSnippet(id='codesnippet-skeleton'),
    ])

stories_dict['node-combobox'] = html.Div([
        html.H2("ComboBox"),
        html.H3("FloatingStyles"),
        carbon_dash.ComboBox(direction='bottom', id='combobox-floatingstyles'),
        html.H3("AllowCustomValue"),
        carbon_dash.ComboBox(id='combobox-allowcustomvalue'),
        html.H3("AutocompleteWithTypeahead"),
        carbon_dash.ComboBox(id='combobox-autocompletewithtypeahead'),
        html.H3("ExperimentalAutoAlign"),
        carbon_dash.ComboBox(id='combobox-experimentalautoalign'),
        html.H3("_WithLayer"),
        carbon_dash.ComboBox(id='combobox-_withlayer'),
        html.H3("withAILabel"),
        carbon_dash.ComboBox(id='combobox-withailabel'),
        html.H3("Controlled"),
        carbon_dash.ComboBox(id='combobox-controlled'),
    ])

stories_dict['node-combobutton'] = html.Div([
        html.H2("ComboButton"),
        html.H3("FloatingStyles"),
        carbon_dash.ComboButton(label='Primary action', children=[carbon_dash.MenuItem(label='Second action with a long label description'), carbon_dash.MenuItem(label='Third action'), carbon_dash.MenuItem(label='Fourth action', disabled=True)], menuAlignment='bottom'),
        html.H3("ExperimentalAutoAlign"),
        carbon_dash.ComboButton(id='combobutton-experimentalautoalign'),
        html.H3("WithDanger"),
        carbon_dash.ComboButton(label='Primary action', children=[carbon_dash.MenuItem(label='Second action with a long label description'), carbon_dash.MenuItem(label='Third action'), carbon_dash.MenuItem(label='Fourth action'), carbon_dash.MenuItemDivider(), carbon_dash.MenuItem(label='Danger action', kind='danger')]),
        html.H3("WithIcons"),
        carbon_dash.ComboButton(label='Save record', children=[carbon_dash.MenuItem(label='Save as a copy', renderIcon=dash_iconify.DashIconify(icon="carbon:copy-file")), carbon_dash.MenuItem(label='Export', renderIcon=dash_iconify.DashIconify(icon="carbon:export"))]),
        html.H3("WithMenuAlignment"),
        carbon_dash.ComboButton(id='combobutton-withmenualignment'),
    ])

stories_dict['node-composedmodal'] = html.Div([
        html.H2("ComposedModal"),
        html.H3("EnableDialogElement"),
        carbon_dash.FeatureFlags(enableDialogElement=True),
        html.H3("EnableFocusWrapWithoutSentinels"),
        carbon_dash.FeatureFlags(enableFocusWrapWithoutSentinels=True),
        html.H3("FullWidth"),
        carbon_dash.ComposedModal(id='composedmodal-fullwidth'),
        html.H3("PassiveModal"),
        carbon_dash.ComposedModal(id='composedmodal-passivemodal'),
        html.H3("WithStateManager"),
        carbon_dash.ComposedModal(id='composedmodal-withstatemanager'),
        html.H3("WithScrollingContent"),
        carbon_dash.ComposedModal(id='composedmodal-withscrollingcontent'),
        html.H3("WithInlineLoading"),
        carbon_dash.ComposedModal(id='composedmodal-withinlineloading'),
        html.H3("_withAILabel"),
        carbon_dash.ComposedModal(id='composedmodal-_withailabel'),
        html.H3("EnablePresence"),
        carbon_dash.FeatureFlags(enablePresence=True),
    ])

stories_dict['node-containedlist'] = html.Div([
        html.H2("ContainedList"),
        html.H3("Default"),
        carbon_dash.ContainedList(label='List title', kind='on-page', size='lg', id='containedlist-default'),
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
        carbon_dash.ContainedList(label='List title', kind='on-page', children=[carbon_dash.ContainedListItem(renderIcon=dash_iconify.DashIconify(icon="carbon:apple"), children='List item'), carbon_dash.ContainedListItem(renderIcon=dash_iconify.DashIconify(icon="carbon:wheat"), children='List item'), carbon_dash.ContainedListItem(renderIcon=dash_iconify.DashIconify(icon="carbon:strawberry"), children='List item'), carbon_dash.ContainedListItem(renderIcon=dash_iconify.DashIconify(icon="carbon:fish"), children='List item')]),
        html.H3("_WithLayer"),
        carbon_dash.ContainedList(id='containedlist-_withlayer'),
        html.H3("UsageExamples"),
        carbon_dash.ContainedList(id='containedlist-usageexamples'),
    ])

stories_dict['node-contentswitcher'] = html.Div([
        html.H2("ContentSwitcher"),
        html.H3("_WithLayer"),
        carbon_dash.ContentSwitcher(id='contentswitcher-_withlayer'),
        html.H3("IconOnly"),
        carbon_dash.ContentSwitcher(children=[carbon_dash.IconSwitch(name='one', text='Table of Contents', children=dash_iconify.DashIconify(icon="carbon:table-of-contents")), carbon_dash.IconSwitch(name='two', text='Workspace Test', children=dash_iconify.DashIconify(icon="carbon:workspace")), carbon_dash.IconSwitch(name='three', text='View Mode', children=dash_iconify.DashIconify(icon="carbon:view-mode_2"))]),
        html.H3("IconOnlyWithLayer"),
        carbon_dash.ContentSwitcher(id='contentswitcher-icononlywithlayer'),
        html.H3("lowContrast"),
        carbon_dash.ContentSwitcher(lowContrast=True, children=[carbon_dash.Switch(name='one', text='First section'), carbon_dash.Switch(name='two', text='Second section'), carbon_dash.Switch(name='three', text='Third section')]),
        html.H3("lowContrastIconOnly"),
        carbon_dash.ContentSwitcher(lowContrast=True, children=[carbon_dash.IconSwitch(name='one', text='Table of Contents', children=dash_iconify.DashIconify(icon="carbon:table-of-contents")), carbon_dash.IconSwitch(name='two', text='Workspace Test', children=dash_iconify.DashIconify(icon="carbon:workspace")), carbon_dash.IconSwitch(name='three', text='View Mode', children=dash_iconify.DashIconify(icon="carbon:view-mode_2"))]),
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
        carbon_dash.Table(children=[carbon_dash.TableHead(children=carbon_dash.TableRow()), carbon_dash.TableBody()], size='xl'),
        html.H3("Default"),
        carbon_dash.DataTable(size='lg', useStaticWidth=False, useZebraStyles=False, isSortable=False, locale='en', radio=False, id='datatable-default'),
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
        carbon_dash.DataTableSkeleton(id='datatableskeleton-skeleton'),
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
        carbon_dash.DatePicker(id='datepicker-simplewithlayer'),
        html.H3("SingleWithCalendarWithLayer"),
        carbon_dash.DatePicker(id='datepicker-singlewithcalendarwithlayer'),
        html.H3("RangeWithCalendarWithLayer"),
        carbon_dash.DatePicker(id='datepicker-rangewithcalendarwithlayer'),
        html.H3("Skeleton"),
        carbon_dash.DatePickerSkeleton(range=True),
        html.H3("withAILabel"),
        carbon_dash.DatePicker(id='datepicker-withailabel'),
    ])

stories_dict['node-dropdown'] = html.Div([
        html.H2("Dropdown"),
        html.H3("FloatingStyles"),
        carbon_dash.Dropdown(direction='bottom', invalid=False, invalidText='Error message goes here', warn=False, warnText='Warning message goes here', id='dropdown-floatingstyles'),
        html.H3("Default"),
        carbon_dash.Dropdown(id='dropdown-default'),
        html.H3("ExperimentalAutoAlign"),
        carbon_dash.Dropdown(invalid=False, invalidText='Error message goes here', warn=False, warnText='Warning message goes here', id='dropdown-experimentalautoalign'),
        html.H3("Inline"),
        carbon_dash.Dropdown(id='dropdown-inline'),
        html.H3("_WithLayer"),
        carbon_dash.Dropdown(invalid=False, invalidText='Error message goes here', warn=False, warnText='Warning message goes here', id='dropdown-_withlayer'),
        html.H3("InlineWithLayer"),
        carbon_dash.Dropdown(id='dropdown-inlinewithlayer'),
        html.H3("Skeleton"),
        carbon_dash.Dropdown(id='dropdown-skeleton'),
        html.H3("withAILabel"),
        carbon_dash.Dropdown(invalid=False, invalidText='Error message goes here', warn=False, warnText='Warning message goes here', id='dropdown-withailabel'),
        html.H3("withToggletipLabel"),
        carbon_dash.Dropdown(id='dropdown-withtoggletiplabel'),
        html.H3("TestInvalidTextNoOverlap"),
        carbon_dash.Dropdown(id='dropdown-testinvalidtextnooverlap'),
    ])

stories_dict['node-errorboundary'] = html.Div([
        html.H2("ErrorBoundary"),
        html.H3("WithCustomContext"),
        carbon_dash.ErrorBoundary(id='errorboundary-withcustomcontext'),
    ])

stories_dict['node-fileuploader'] = html.Div([
        html.H2("FileUploader"),
        html.H3("EnhancedCallbacks"),
        carbon_dash.FileUploader(disabled=False, id='fileuploader-enhancedcallbacks'),
        html.H3("_FileUploaderItem"),
        carbon_dash.FileUploaderItem(errorBody='1 MB max file size. Select a new file and try again.', errorSubject='File size exceeds limit', iconDescription='Delete file', invalid=False, name='THIS IS A VERY LONG FILENAME WHICH WILL BE TRUNCATED', status='edit', size='md'),
        html.H3("_FileUploaderDropContainer"),
        carbon_dash.FileUploaderDropContainer(labelText='Drag and drop files here or click to upload', multiple=True, disabled=False, name=''),
        html.H3("DragAndDropUploadContainerExampleApplication"),
        carbon_dash.FileUploader(name='', multiple=True, disabled=False, id='fileuploader-draganddropuploadcontainerexampleapplication'),
        html.H3("DragAndDropUploadSingleContainerExampleApplication"),
        carbon_dash.FileUploader(name='', multiple=False, disabled=False, id='fileuploader-draganddropuploadsinglecontainerexampleapplication'),
        html.H3("Skeleton"),
        carbon_dash.FileUploader(id='fileuploader-skeleton'),
        html.H3("Default"),
        carbon_dash.FileUploader(labelTitle='Upload files', labelDescription='Max file size is 1 MB. Only .jpg files are supported.', buttonLabel='Add file', buttonKind='primary', size='md', filenameStatus='edit', multiple=True, disabled=False, iconDescription='Delete file', name='', id='fileuploader-default'),
    ])

stories_dict['node-fluidcombobox'] = html.Div([
        html.H2("FluidComboBox"),
        html.H3("Default"),
        carbon_dash.FluidComboBox(className='test-class', isCondensed=False, disabled=False, invalid=False, invalidText='Error message that is really long can wrap to more lines but should not be excessively long.', label='Choose an option', titleText='Label', warn=False, warnText='Warning message that is really long can wrap to more lines but should not be excessively long.', id='fluidcombobox-default'),
        html.H3("Condensed"),
        carbon_dash.FluidComboBox(id='fluidcombobox-condensed'),
        html.H3("withAILabel"),
        carbon_dash.FluidComboBox(id='fluidcombobox-withailabel'),
        html.H3("Skeleton"),
        carbon_dash.FluidComboBox(id='fluidcombobox-skeleton'),
    ])

stories_dict['node-fluiddatepicker'] = html.Div([
        html.H2("FluidDatePicker"),
        html.H3("Simple"),
        carbon_dash.FluidDatePicker(id='fluiddatepicker-simple'),
        html.H3("Single"),
        carbon_dash.FluidDatePicker(id='fluiddatepicker-single'),
        html.H3("RangeWithCalendar"),
        carbon_dash.FluidDatePicker(id='fluiddatepicker-rangewithcalendar'),
        html.H3("Skeleton"),
        carbon_dash.FluidDatePicker(id='fluiddatepicker-skeleton'),
    ])

stories_dict['node-fluiddropdown'] = html.Div([
        html.H2("FluidDropdown"),
        html.H3("Default"),
        carbon_dash.FluidDropdown(className='test-class', isCondensed=False, disabled=False, invalid=False, invalidText='Error message that is really long can wrap to more lines but should not be excessively long.', label='Choose an option', titleText='Label', warn=False, warnText='Warning message that is really long can wrap to more lines but should not be excessively long.', id='fluiddropdown-default'),
        html.H3("Condensed"),
        carbon_dash.FluidDropdown(id='fluiddropdown-condensed'),
        html.H3("withAILabel"),
        carbon_dash.FluidDropdown(id='fluiddropdown-withailabel'),
        html.H3("Skeleton"),
        carbon_dash.FluidDropdown(id='fluiddropdown-skeleton'),
    ])

stories_dict['node-fluidmultiselect'] = html.Div([
        html.H2("FluidMultiSelect"),
        html.H3("Default"),
        carbon_dash.FluidMultiSelect(className='test-class', isCondensed=False, isFilterable=False, disabled=False, invalid=False, invalidText='Error message that is really long can wrap to more lines but should not be excessively long.', label='Choose an option', titleText='Label', warn=False, warnText='Warning message that is really long can wrap to more lines but should not be excessively long.', id='fluidmultiselect-default'),
        html.H3("Filterable"),
        carbon_dash.FluidMultiSelect(id='fluidmultiselect-filterable'),
        html.H3("_FilterableWithLayer"),
        carbon_dash.FluidMultiSelect(id='fluidmultiselect-_filterablewithlayer'),
        html.H3("Condensed"),
        carbon_dash.FluidMultiSelect(id='fluidmultiselect-condensed'),
        html.H3("withAILabel"),
        carbon_dash.FluidMultiSelect(id='fluidmultiselect-withailabel'),
        html.H3("Skeleton"),
        carbon_dash.FluidMultiSelect(id='fluidmultiselect-skeleton'),
    ])

stories_dict['node-fluidnumberinput'] = html.Div([
        html.H2("FluidNumberInput"),
        html.H3("Default"),
        carbon_dash.FluidNumberInput(max=100, min=0, step=10, id='input-default', defaultValue=50, invalid=False, invalidText='Error message that is really long can wrap to more lines but should not be excessively long.', disabled=False, warn=False, warnText='Warning message that is really long can wrap to more lines but should not be excessively long.'),
        html.H3("Skeleton"),
        carbon_dash.FluidNumberInput(id='fluidnumberinput-skeleton'),
    ])

stories_dict['node-fluidsearch'] = html.Div([
        html.H2("FluidSearch"),
        html.H3("Skeleton"),
        carbon_dash.FluidSearch(id='fluidsearch-skeleton'),
        html.H3("Default"),
        carbon_dash.FluidSearch(closeButtonLabelText='Clear search input', disabled=False, labelText='Search', placeholder='Prompt text', id='fluidsearch-default'),
    ])

stories_dict['node-fluidselect'] = html.Div([
        html.H2("FluidSelect"),
        html.H3("Default"),
        carbon_dash.FluidSelect(className='test-class', disabled=False, invalid=False, invalidText='Error message that is really long can wrap to more lines but should not be excessively long.', warn=False, warnText='Warning message that is really long can wrap to more lines but should not be excessively long.', id='fluidselect-default'),
        html.H3("withAILabel"),
        carbon_dash.FluidSelect(id='fluidselect-withailabel'),
        html.H3("Skeleton"),
        carbon_dash.FluidSelect(id='fluidselect-skeleton'),
    ])

stories_dict['node-fluidtextarea'] = html.Div([
        html.H2("FluidTextArea"),
        html.H3("Default"),
        carbon_dash.FluidTextArea(className='test-class', placeholder='Placeholder text', invalid=False, invalidText='Error message that is really long can wrap to more lines but should not be excessively long.', disabled=False, enableCounter=False, labelText='Text Area label', maxCount=500, warn=False, warnText='This is a warning message.', id='fluidtextarea-default'),
        html.H3("DefaultWithLayers"),
        carbon_dash.FluidTextArea(id='fluidtextarea-defaultwithlayers'),
        html.H3("DefaultWithToggletip"),
        carbon_dash.FluidTextArea(placeholder='Placeholder text'),
        html.H3("Skeleton"),
        carbon_dash.FluidTextArea(id='fluidtextarea-skeleton'),
    ])

stories_dict['node-fluidtextinput'] = html.Div([
        html.H2("FluidTextInput"),
        html.H3("Default"),
        carbon_dash.FluidTextInput(placeholder='Placeholder text', invalid=False, invalidText='Error message that is really long can wrap to more lines but should not be excessively long.', disabled=False, labelText='Label', warn=False, warnText='Warning message that is really long can wrap to more lines but should not be excessively long.', id='fluidtextinput-default'),
        html.H3("DefaultWithToggletip"),
        carbon_dash.FluidTextInput(placeholder='Placeholder text'),
        html.H3("Skeleton"),
        carbon_dash.FluidTextInput(id='fluidtextinput-skeleton'),
    ])

stories_dict['node-fluidtimepicker'] = html.Div([
        html.H2("FluidTimePicker"),
        html.H3("Skeleton"),
        carbon_dash.FluidTimePicker(id='fluidtimepicker-skeleton'),
        html.H3("Default"),
        carbon_dash.FluidTimePicker(labelText='Time', invalidText='Error message that is really long can wrap to more lines but should not be excessively long.', warnText='Warning message that is really long can wrap to more lines but should not be excessively long.', id='fluidtimepicker-default'),
    ])

stories_dict['node-form'] = html.Div([
        html.H2("Form"),
        html.H3("withAILabel"),
        carbon_dash.Stack(gap=7, className='form-example', children=[carbon_dash.Form(className='ai-label-form', children=carbon_dash.Stack(gap=7, children=[carbon_dash.NumberInput(), carbon_dash.DatePicker(datePickerType='single', children=carbon_dash.DatePickerInput(placeholder='mm/dd/yyyy', labelText='Date Picker label', size='md', id='date-picker')), carbon_dash.TextInput(), carbon_dash.TextArea(), carbon_dash.Dropdown(id='default', titleText='Dropdown title', helperText='This is some helper text', label='Option 1'), carbon_dash.MultiSelect(label='Multiselect Label', id='carbon-multiselect-example', titleText='Multiselect title', helperText='This is helper text', selectionFeedback='top-after-reopen'), carbon_dash.FilterableMultiSelect(id='carbon-multiselect-example-3', titleText='FilterableMultiselect title', selectionFeedback='top-after-reopen'), carbon_dash.ComboBox(id='carbon-combobox', titleText='ComboBox title', helperText='Combobox helper text'), carbon_dash.Select(id='select-1', labelText='Select an option', helperText='Optional helper text', children=[carbon_dash.SelectItem(value='', text=''), carbon_dash.SelectItem(value='An example option that is really long to show what should be done to handle long text', text='An example option that is really long to show what should be done to handle long text'), carbon_dash.SelectItem(value='Option 2', text='Option 2'), carbon_dash.SelectItem(value='Option 3', text='Option 3'), carbon_dash.SelectItem(value='Option 4', text='Option 4')]), carbon_dash.Button(type='submit', className='some-class', children='Submit')])), carbon_dash.FluidForm(className='fluid-ai-label-form', children=carbon_dash.Button(type='submit', className='some-class', children='Submit'))]),
    ])

stories_dict['node-formgroup'] = html.Div([
        html.H2("FormGroup"),
        html.H3("Default"),
        carbon_dash.FormGroup(legendId='form-group-1', legendText='FormGroup Legend', message=False, id='formgroup-default'),
    ])

stories_dict['node-formlabel'] = html.Div([
        html.H2("FormLabel"),
        html.H3("WithToggletip"),
        carbon_dash.FormLabel(id='formlabel-withtoggletip'),
    ])

stories_dict['node-grid'] = html.Div([
        html.H2("Grid"),
        html.H3("AutoColumns"),
        carbon_dash.Grid(id='grid-autocolumns'),
        html.H3("ResponsiveGrid"),
        carbon_dash.Grid(id='grid-responsivegrid'),
        html.H3("Offset"),
        carbon_dash.Grid(id='grid-offset'),
        html.H3("Condensed"),
        carbon_dash.Grid(id='grid-condensed'),
        html.H3("CondensedColumns"),
        carbon_dash.Grid(id='grid-condensedcolumns'),
        html.H3("Narrow"),
        carbon_dash.Grid(id='grid-narrow'),
        html.H3("NarrowColumns"),
        carbon_dash.Grid(id='grid-narrowcolumns'),
        html.H3("FullWidth"),
        carbon_dash.Grid(id='grid-fullwidth'),
        html.H3("MixedGutterModes"),
        carbon_dash.Grid(id='grid-mixedguttermodes'),
        html.H3("Default"),
        carbon_dash.Grid(as_='div', fullWidth=False, narrow=False, condensed=False, id='grid-default'),
        html.H3("Responsive"),
        carbon_dash.Grid(id='grid-responsive'),
        html.H3("Subgrid"),
        carbon_dash.Grid(id='grid-subgrid'),
        html.H3("GridStartEnd"),
        carbon_dash.Grid(id='grid-gridstartend'),
        html.H3("WithGridSettings"),
        carbon_dash.Grid(id='grid-withgridsettings'),
    ])

stories_dict['node-heading'] = html.Div([
        html.H2("Heading"),
        html.H3("CustomLevel"),
        carbon_dash.Heading(id='heading-customlevel'),
    ])

stories_dict['node-iconbutton'] = html.Div([
        html.H2("IconButton"),
        html.H3("Default"),
        carbon_dash.IconButton(align='bottom', defaultOpen=True, disabled=False, label='Custom label', kind='primary', id='iconbutton-default'),
        html.H3("withBadgeIndicator"),
        carbon_dash.IconButton(badgeCount=4, id='iconbutton-withbadgeindicator'),
    ])

stories_dict['node-inlineloading'] = html.Div([
        html.H2("InlineLoading"),
        html.H3("UxExample"),
        carbon_dash.InlineLoading(id='inlineloading-uxexample'),
        html.H3("Default"),
        carbon_dash.InlineLoading(description='Loading', iconDescription='Loading data...', id='inlineloading-default'),
    ])

stories_dict['node-layer'] = html.Div([
        html.H2("Layer"),
        html.H3("withBackground"),
        carbon_dash.Layer(id='layer-withbackground'),
        html.H3("CustomLevel"),
        carbon_dash.Layer(level=2),
        html.H3("UseLayer"),
        carbon_dash.Layer(id='layer-uselayer'),
    ])

stories_dict['node-link'] = html.Div([
        html.H2("Link"),
        html.H3("Inline"),
        carbon_dash.Link(inline=True, id='link-inline'),
        html.H3("PairedWithIcon"),
        carbon_dash.Link(href='#', children='Carbon Docs'),
    ])

stories_dict['node-loading'] = html.Div([
        html.H2("Loading"),
        html.H3("Default"),
        carbon_dash.Loading(active=True, withOverlay=False, small=False, description='Loading', id='loading-default'),
    ])

stories_dict['node-menu'] = html.Div([
        html.H2("Menu"),
        html.H3("Default"),
        carbon_dash.Menu(open=True, id='menu-default'),
    ])

stories_dict['node-menubutton'] = html.Div([
        html.H2("MenuButton"),
        html.H3("FloatingStyles"),
        carbon_dash.MenuButton(label='Actions', children=[carbon_dash.MenuItem(label='First action'), carbon_dash.MenuItem(label='Second action that is a longer item to test overflow and title.'), carbon_dash.MenuItem(label='Third action', disabled=True)], menuAlignment='bottom'),
        html.H3("Default"),
        carbon_dash.MenuButton(label='Actions', id='menubutton-default'),
        html.H3("ExperimentalAutoAlign"),
        carbon_dash.MenuButton(id='menubutton-experimentalautoalign'),
        html.H3("WithDanger"),
        carbon_dash.MenuButton(label='Actions', children=[carbon_dash.MenuItem(label='First action'), carbon_dash.MenuItem(label='Second action'), carbon_dash.MenuItem(label='Third action'), carbon_dash.MenuItemDivider(), carbon_dash.MenuItem(label='Danger action', kind='danger')]),
        html.H3("WithDividers"),
        carbon_dash.MenuButton(label='Actions', children=[carbon_dash.MenuItem(label='Create service request'), carbon_dash.MenuItem(label='Create work order'), carbon_dash.MenuItemDivider(), carbon_dash.MenuItem(label='Add plan'), carbon_dash.MenuItem(label='Add flag'), carbon_dash.MenuItemDivider(), carbon_dash.MenuItem(label='Edit source location'), carbon_dash.MenuItem(label='Recalculate source')]),
        html.H3("WithIcons"),
        carbon_dash.MenuButton(label='Add', children=[carbon_dash.MenuItem(label='Asset', renderIcon=dash_iconify.DashIconify(icon="carbon:asset")), carbon_dash.MenuItem(label='User', renderIcon=dash_iconify.DashIconify(icon="carbon:user")), carbon_dash.MenuItem(label='User group', renderIcon=dash_iconify.DashIconify(icon="carbon:group"))]),
        html.H3("WithNestedMenu"),
        carbon_dash.MenuButton(label='Actions', children=[carbon_dash.MenuItem(label='Save', shortcut='⌘S'), carbon_dash.MenuItem(label='Save as', shortcut='⌥⌘S'), carbon_dash.MenuItem(label='Export as', children=[carbon_dash.MenuItem(label='PDF'), carbon_dash.MenuItem(label='JPG'), carbon_dash.MenuItem(label='PNG')]), carbon_dash.MenuItemDivider(), carbon_dash.MenuItem(label='Delete', kind='danger')]),
        html.H3("WithMenuAlignment"),
        carbon_dash.MenuButton(id='menubutton-withmenualignment'),
    ])

stories_dict['node-modal'] = html.Div([
        html.H2("Modal"),
        html.H3("EnableDialogElement"),
        carbon_dash.FeatureFlags(enableDialogElement=True),
        html.H3("EnableFocusWrapWithoutSentinels"),
        carbon_dash.FeatureFlags(enableFocusWrapWithoutSentinels=True),
        html.H3("FullWidth"),
        carbon_dash.Modal(id='modal-fullwidth'),
        html.H3("DangerModal"),
        carbon_dash.Modal(id='modal-dangermodal'),
        html.H3("WithScrollingContent"),
        carbon_dash.Modal(id='modal-withscrollingcontent'),
        html.H3("WithStateManager"),
        carbon_dash.Modal(id='modal-withstatemanager'),
        html.H3("PassiveModal"),
        carbon_dash.Modal(id='modal-passivemodal'),
        html.H3("WithInlineLoading"),
        carbon_dash.Modal(id='modal-withinlineloading'),
        html.H3("withAILabel"),
        carbon_dash.Modal(id='modal-withailabel'),
        html.H3("EnablePresence"),
        carbon_dash.FeatureFlags(enablePresence=True),
    ])

stories_dict['node-multiselect'] = html.Div([
        html.H2("MultiSelect"),
        html.H3("FloatingStyles"),
        carbon_dash.MultiSelect(id='carbon-multiselect-example', selectionFeedback='top-after-reopen', direction='bottom'),
        html.H3("Default"),
        carbon_dash.MultiSelect(id='multiselect-default'),
        html.H3("WithInitialSelectedItems"),
        carbon_dash.MultiSelect(id='multiselect-withinitialselecteditems'),
        html.H3("Filterable"),
        carbon_dash.MultiSelect(id='multiselect-filterable'),
        html.H3("FilterableWithSelectAll"),
        carbon_dash.MultiSelect(id='multiselect-filterablewithselectall'),
        html.H3("WithLayerMultiSelect"),
        carbon_dash.MultiSelect(id='multiselect-withlayermultiselect'),
        html.H3("_FilterableWithLayer"),
        carbon_dash.MultiSelect(id='multiselect-_filterablewithlayer'),
        html.H3("_Controlled"),
        carbon_dash.MultiSelect(id='multiselect-_controlled'),
        html.H3("SelectAll"),
        carbon_dash.MultiSelect(id='multiselect-selectall'),
        html.H3("withAILabel"),
        carbon_dash.MultiSelect(id='multiselect-withailabel'),
        html.H3("FilterableWithAILabel"),
        carbon_dash.MultiSelect(id='multiselect-filterablewithailabel'),
        html.H3("ExperimentalAutoAlign"),
        carbon_dash.MultiSelect(autoAlign=True, id='multiselect-experimentalautoalign'),
        html.H3("withToggletipLabel"),
        carbon_dash.MultiSelect(id='multiselect-withtoggletiplabel'),
        html.H3("SelectAllWithDynamicItems"),
        carbon_dash.MultiSelect(id='multiselect-selectallwithdynamicitems'),
    ])

stories_dict['node-numberinput'] = html.Div([
        html.H2("NumberInput"),
        html.H3("Default"),
        carbon_dash.NumberInput(step=1, disabled=False, invalid=False, helperText='Optional helper text.', warn=False, warnText='Warning message that is really long can wrap to more lines but should not be excessively long.', size='md', id='numberinput-default'),
        html.H3("withAILabel"),
        carbon_dash.NumberInput(id='numberinput-withailabel'),
        html.H3("WithTypeOfText"),
        carbon_dash.NumberInput(id='default-number-input', inputMode='decimal', defaultValue=50, label='NumberInput label', helperText='Optional helper text.', step=1, disabled=False, invalid=False, warn=False, warnText='Warning message that is really long can wrap to more lines but should not be excessively long.', size='md', type='text'),
        html.H3("WithTypeOfTextControlled"),
        carbon_dash.NumberInput(step=1, disabled=False, invalid=False, helperText='Optional helper text.', warn=False, warnText='Warning message that is really long can wrap to more lines but should not be excessively long.', size='md', type='text', id='numberinput-withtypeoftextcontrolled'),
        html.H3("WithTypeOfCustomValidation"),
        carbon_dash.NumberInput(step=1, disabled=False, invalid=False, helperText='Optional helper text.', warn=False, warnText='Warning message that is really long can wrap to more lines but should not be excessively long.', size='md', type='text', id='numberinput-withtypeofcustomvalidation'),
        html.H3("Skeleton"),
        carbon_dash.NumberInputSkeleton(),
    ])

stories_dict['node-orderedlist'] = html.Div([
        html.H2("OrderedList"),
        html.H3("Default"),
        carbon_dash.OrderedList(isExpressive=False, native=False, nested=False, id='orderedlist-default'),
        html.H3("Nested"),
        carbon_dash.OrderedList(children=[carbon_dash.ListItem(children=['Ordered List level 1', carbon_dash.OrderedList(nested=True, children=[carbon_dash.ListItem(children='Ordered List level 2'), carbon_dash.ListItem(children=['Ordered List level 2', carbon_dash.OrderedList(nested=True, children=[carbon_dash.ListItem(children='Ordered List level 3'), carbon_dash.ListItem(children='Ordered List level 3')])])])]), carbon_dash.ListItem(children='Ordered List level 1'), carbon_dash.ListItem(children='Ordered List level 1')]),
        html.H3("NativeListStyles"),
        carbon_dash.OrderedList(native=True, children=[carbon_dash.ListItem(children='Ordered List level 1'), carbon_dash.ListItem(children='Ordered List level 1'), carbon_dash.ListItem(children='Ordered List level 1'), carbon_dash.ListItem(children=['Ordered List level 1', carbon_dash.OrderedList(nested=True, children=[carbon_dash.ListItem(children='Ordered List level 2'), carbon_dash.ListItem(children='Ordered List level 2'), carbon_dash.ListItem(children='Ordered List level 2'), carbon_dash.ListItem(children='Ordered List level 2')])]), carbon_dash.ListItem(children='Ordered List level 1'), carbon_dash.ListItem(children='Ordered List level 1'), carbon_dash.ListItem(children='Ordered List level 1'), carbon_dash.ListItem(children='Ordered List level 1'), carbon_dash.ListItem(children='Ordered List level 1'), carbon_dash.ListItem(children='Ordered List level 1'), carbon_dash.ListItem(children='Ordered List level 1'), carbon_dash.ListItem(children='Ordered List level 1')]),
    ])

stories_dict['node-overflowmenu'] = html.Div([
        html.H2("OverflowMenu"),
        html.H3("AutoAlign"),
        carbon_dash.OverflowMenu(id='overflowmenu-autoalign'),
        html.H3("Nested"),
        carbon_dash.FeatureFlags(children=carbon_dash.OverflowMenu(children=[carbon_dash.MenuItem(label='Level 1'), carbon_dash.MenuItem(label='Level 1'), carbon_dash.MenuItem(label='Level 1', children=[carbon_dash.MenuItem(label='Level 2', children=[carbon_dash.MenuItem(label='Level 3'), carbon_dash.MenuItem(label='Level 3', children=carbon_dash.MenuItem(label='Level 4'))]), carbon_dash.MenuItem(label='Level 2'), carbon_dash.MenuItem(label='Level 2')]), carbon_dash.MenuItem(label='Level 1')])),
        html.H3("WithMenuAlignment"),
        carbon_dash.OverflowMenu(id='overflowmenu-withmenualignment'),
        html.H3("FloatingStyles"),
        carbon_dash.OverflowMenu(id='overflowmenu-floatingstyles'),
        html.H3("Default"),
        carbon_dash.OverflowMenu(focusTrap=False, open=False, id='overflowmenu-default'),
        html.H3("RenderCustomIcon"),
        carbon_dash.OverflowMenu(renderIcon=dash_iconify.DashIconify(icon="carbon:filter"), children=[carbon_dash.OverflowMenuItem(itemText='Filter A'), carbon_dash.OverflowMenuItem(itemText='Filter B')]),
    ])

stories_dict['node-pagination'] = html.Div([
        html.H2("Pagination"),
        html.H3("Default"),
        carbon_dash.Pagination(backwardText='Previous', forwardText='Next', disabled=False, isLastPage=False, itemsPerPageText='Items per page:', page=1, pageInputDisabled=False, pageSize=10, pageNumberText='Page Number', pagesUnknown=False, pageSizeInputDisabled=False, totalItems=103, id='pagination-default'),
        html.H3("MultiplePaginationComponents"),
        carbon_dash.Pagination(id='pagination-multiplepaginationcomponents'),
        html.H3("PaginationWithCustomPageSizesLabel"),
        carbon_dash.Pagination(id='pagination-paginationwithcustompagesizeslabel'),
        html.H3("PaginationUnknownPages"),
        carbon_dash.Pagination(id='pagination-paginationunknownpages'),
    ])

stories_dict['node-paginationnav'] = html.Div([
        html.H2("PaginationNav"),
        html.H3("Default"),
        carbon_dash.PaginationNav(size='lg', loop=False, itemsShown=10, page=0, totalItems=25, disableOverflow=False, id='paginationnav-default'),
    ])

stories_dict['node-popover'] = html.Div([
        html.H2("Popover"),
        html.H3("FloatingStyles"),
        carbon_dash.Popover(align='bottom', id='popover-floatingstyles'),
        html.H3("TabTip"),
        carbon_dash.Popover(id='popover-tabtip'),
        html.H3("Default"),
        carbon_dash.Popover(caret=True, dropShadow=True, highContrast=False, open=True, id='popover-default'),
        html.H3("ExperimentalAutoAlign"),
        carbon_dash.Popover(id='popover-experimentalautoalign'),
        html.H3("ExperimentalAutoAlignBoundary"),
        carbon_dash.Popover(id='popover-experimentalautoalignboundary'),
        html.H3("TabTipExperimentalAutoAlign"),
        carbon_dash.Popover(id='popover-tabtipexperimentalautoalign'),
    ])

stories_dict['node-progressbar'] = html.Div([
        html.H2("ProgressBar"),
        html.H3("Indeterminate"),
        carbon_dash.ProgressBar(label='Progress bar label', helperText='Optional helper text'),
        html.H3("Determinate"),
        carbon_dash.ProgressBar(label='Export data'),
        html.H3("_WithLayer"),
        carbon_dash.ProgressBar(id='progressbar-_withlayer'),
    ])

stories_dict['node-progressindicator'] = html.Div([
        html.H2("ProgressIndicator"),
        html.H3("Interactive"),
        carbon_dash.ProgressIndicator(currentIndex=1, children=[carbon_dash.ProgressStep(label='Click me', description='Step 1: Register an onChange event'), carbon_dash.ProgressStep(label='Really long label', description='The progress indicator will listen for clicks on the steps'), carbon_dash.ProgressStep(label='Third step', description='The progress indicator will listen for clicks on the steps')]),
        html.H3("Skeleton"),
        carbon_dash.ProgressIndicatorSkeleton(),
        html.H3("Default"),
        carbon_dash.ProgressIndicator(currentIndex=0, spaceEqually=False, vertical=False, id='progressindicator-default'),
    ])

stories_dict['node-radiobutton'] = html.Div([
        html.H2("RadioButton"),
        html.H3("Vertical"),
        carbon_dash.RadioButtonGroup(legendText='Group label', name='radio-button-vertical-group', defaultSelected='radio-1', orientation='vertical', children=[carbon_dash.RadioButton(labelText='Radio button label', value='radio-1', id='radio-1'), carbon_dash.RadioButton(labelText='Radio button label', value='radio-2', id='radio-2'), carbon_dash.RadioButton(labelText='Radio button label', value='radio-3', id='radio-3', disabled=True)]),
        html.H3("Skeleton"),
        carbon_dash.RadioButtonSkeleton(),
        html.H3("withAILabel"),
        carbon_dash.RadioButton(id='radiobutton-withailabel'),
        html.H3("Default"),
        carbon_dash.RadioButton(hideLabel=False, invalidText='Invalid selection', warn=False, warnText='Please notice the warning', id='radiobutton-default'),
    ])

stories_dict['node-search'] = html.Div([
        html.H2("Search"),
        html.H3("Disabled"),
        carbon_dash.Search(disabled=True, size='lg', placeholder='Find your items', labelText='Search', closeButtonLabelText='Clear search input', id='search-1'),
        html.H3("Expandable"),
        carbon_dash.Search(id='search-expandable'),
        html.H3("_WithLayer"),
        carbon_dash.Search(id='search-_withlayer'),
        html.H3("ExpandableWithLayer"),
        carbon_dash.Search(id='search-expandablewithlayer'),
        html.H3("Default"),
        carbon_dash.Search(closeButtonLabelText='Clear search input', disabled=False, labelText='Label text', placeholder='Placeholder text', size='md', type='search', id='search-default'),
    ])

stories_dict['node-select'] = html.Div([
        html.H2("Select"),
        html.H3("Inline"),
        carbon_dash.Select(inline=True, id='select-inline'),
        html.H3("Skeleton"),
        carbon_dash.SelectSkeleton(),
        html.H3("_WithLayer"),
        carbon_dash.Select(id='select-_withlayer'),
        html.H3("withAILabel"),
        carbon_dash.Select(id='select-withailabel'),
    ])

stories_dict['node-skeletontext'] = html.Div([
        html.H2("SkeletonText"),
        html.H3("Default"),
        carbon_dash.SkeletonText(heading=False, paragraph=False, width='100%', lineCount=3, id='skeletontext-default'),
    ])

stories_dict['node-slider'] = html.Div([
        html.H2("Slider"),
        html.H3("Default"),
        carbon_dash.Slider(ariaLabelInput='Lower bound', unstable_ariaLabelInputUpper='Upper bound', disabled=False, hideTextInput=False, invalid=False, invalidText='Invalid message goes here', min=0, max=100, readOnly=False, required=False, step=5, stepMultiplier=5, value=50, warn=False, warnText='Warning message goes here', id='slider-default'),
        html.H3("SliderWithHiddenInputs"),
        carbon_dash.Slider(labelText='Slider label', value=50, min=0, max=100, step=1, stepMultiplier=10, invalidText='Invalid message goes here', hideTextInput=True),
        html.H3("SliderWithCustomValueLabel"),
        carbon_dash.Slider(labelText='Slider label with low/medium/high', value=50, min=0, max=100, stepMultiplier=50, step=1, hideTextInput=True),
        html.H3("ControlledSlider"),
        carbon_dash.Slider(id='slider-controlledslider'),
        html.H3("_WithLayer"),
        carbon_dash.Slider(id='slider-_withlayer'),
        html.H3("ControlledSliderWithLayer"),
        carbon_dash.Slider(id='slider-controlledsliderwithlayer'),
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
        carbon_dash.Stack(gap=6, orientation='horizontal'),
        html.H3("Default"),
        carbon_dash.Stack(as_='div', id='stack-default'),
    ])

stories_dict['node-tabs'] = html.Div([
        html.H2("Tabs"),
        html.H3("Default"),
        carbon_dash.Tabs(dismissable=False, id='tabs-default'),
        html.H3("Dismissable"),
        carbon_dash.Tabs(id='tabs-dismissable'),
        html.H3("DismissableContained"),
        carbon_dash.Tabs(id='tabs-dismissablecontained'),
        html.H3("DismissableWithIcons"),
        carbon_dash.Tabs(id='tabs-dismissablewithicons'),
        html.H3("WithIcons"),
        carbon_dash.Tabs(children=[carbon_dash.TabList(activation='manual', children=[carbon_dash.Tab(renderIcon=dash_iconify.DashIconify(icon="carbon:dashboard"), children='Dashboard'), carbon_dash.Tab(renderIcon=dash_iconify.DashIconify(icon="carbon:cloud-monitoring"), children='Monitoring'), carbon_dash.Tab(renderIcon=dash_iconify.DashIconify(icon="carbon:activity"), children='Activity'), carbon_dash.Tab(renderIcon=dash_iconify.DashIconify(icon="carbon:ibm-watson-discovery"), children='Analyze'), carbon_dash.Tab(disabled=True, renderIcon=dash_iconify.DashIconify(icon="carbon:settings"), children='Settings')]), carbon_dash.TabPanels(children=[carbon_dash.TabPanel(children='Tab Panel 1'), carbon_dash.TabPanel(), carbon_dash.TabPanel(children='Tab Panel 3'), carbon_dash.TabPanel(children='Tab Panel 4'), carbon_dash.TabPanel(children='Tab Panel 5')])]),
        html.H3("Manual"),
        carbon_dash.Tabs(children=[carbon_dash.TabList(activation='manual', children=[carbon_dash.Tab(children='Dashboard'), carbon_dash.Tab(children='Monitoring'), carbon_dash.Tab(children='Activity'), carbon_dash.Tab(children='Analyze'), carbon_dash.Tab(disabled=True, children='Settings')]), carbon_dash.TabPanels(children=[carbon_dash.TabPanel(children='Tab Panel 1'), carbon_dash.TabPanel(), carbon_dash.TabPanel(children='Tab Panel 3'), carbon_dash.TabPanel(children='Tab Panel 4'), carbon_dash.TabPanel(children='Tab Panel 5')])]),
        html.H3("Icon20Only"),
        carbon_dash.Tabs(children=[carbon_dash.TabList(iconSize='lg', children=[carbon_dash.IconTab(label='Analyze', children=dash_iconify.DashIconify(icon="carbon:ibm-watson-discovery")), carbon_dash.IconTab(label='Activity', children=dash_iconify.DashIconify(icon="carbon:activity")), carbon_dash.IconTab(label='New Notifications', children=dash_iconify.DashIconify(icon="carbon:notification")), carbon_dash.IconTab(label='Chat', children=dash_iconify.DashIconify(icon="carbon:chat"))]), carbon_dash.TabPanels(children=[carbon_dash.TabPanel(children='Tab Panel 1'), carbon_dash.TabPanel(children='Tab Panel 2'), carbon_dash.TabPanel(children='Tab Panel 3'), carbon_dash.TabPanel(children='Tab Panel 4')])]),
        html.H3("IconOnly"),
        carbon_dash.Tabs(children=[carbon_dash.TabList(iconSize='default', children=[carbon_dash.IconTab(label='Analyze', children=dash_iconify.DashIconify(icon="carbon:ibm-watson-discovery")), carbon_dash.IconTab(label='Activity', children=dash_iconify.DashIconify(icon="carbon:activity")), carbon_dash.IconTab(label='New Notifications', children=dash_iconify.DashIconify(icon="carbon:notification")), carbon_dash.IconTab(label='Chat', children=dash_iconify.DashIconify(icon="carbon:chat"))]), carbon_dash.TabPanels(children=[carbon_dash.TabPanel(children='Tab Panel 1'), carbon_dash.TabPanel(children='Tab Panel 2'), carbon_dash.TabPanel(children='Tab Panel 3'), carbon_dash.TabPanel(children='Tab Panel 4')])]),
        html.H3("Contained"),
        carbon_dash.Tabs(children=[carbon_dash.TabList(contained=True, children=[carbon_dash.Tab(children='Dashboard'), carbon_dash.Tab(children='Monitoring'), carbon_dash.Tab(children='Activity'), carbon_dash.Tab(children='Analyze'), carbon_dash.Tab(disabled=True, children='Settings')]), carbon_dash.TabPanels(children=[carbon_dash.TabPanel(children='Tab Panel 1'), carbon_dash.TabPanel(children=carbon_dash.Layer()), carbon_dash.TabPanel(children='Tab Panel 3'), carbon_dash.TabPanel(children='Tab Panel 4'), carbon_dash.TabPanel(children='Tab Panel 5')])]),
        html.H3("ContainedWithIcons"),
        carbon_dash.Tabs(children=[carbon_dash.TabList(contained=True, children=[carbon_dash.Tab(renderIcon=dash_iconify.DashIconify(icon="carbon:dashboard"), children='Dashboard'), carbon_dash.Tab(renderIcon=dash_iconify.DashIconify(icon="carbon:cloud-monitoring"), children='Monitoring'), carbon_dash.Tab(renderIcon=dash_iconify.DashIconify(icon="carbon:activity"), children='Activity'), carbon_dash.Tab(renderIcon=dash_iconify.DashIconify(icon="carbon:ibm-watson-discovery"), children='Analyze'), carbon_dash.Tab(disabled=True, renderIcon=dash_iconify.DashIconify(icon="carbon:settings"), children='Settings')]), carbon_dash.TabPanels(children=[carbon_dash.TabPanel(children='Tab Panel 1'), carbon_dash.TabPanel(children=carbon_dash.Layer()), carbon_dash.TabPanel(children='Tab Panel 3'), carbon_dash.TabPanel(children='Tab Panel 4'), carbon_dash.TabPanel(children='Tab Panel 5')])]),
        html.H3("ContainedWithSecondaryLabels"),
        carbon_dash.Tabs(children=[carbon_dash.TabList(contained=True, children=[carbon_dash.Tab(secondaryLabel='(21/25)', children='Engage'), carbon_dash.Tab(secondaryLabel='(12/16)', children='Analyze'), carbon_dash.Tab(secondaryLabel='(0/7)', children='Remediate'), carbon_dash.Tab(secondaryLabel='(4/12)', children='Assets'), carbon_dash.Tab(disabled=True, secondaryLabel='(0/10)', children='Monitoring')]), carbon_dash.TabPanels(children=[carbon_dash.TabPanel(children='Tab Panel 1'), carbon_dash.TabPanel(children=carbon_dash.Layer()), carbon_dash.TabPanel(children='Tab Panel 3'), carbon_dash.TabPanel(children='Tab Panel 4'), carbon_dash.TabPanel(children='Tab Panel 5')])]),
        html.H3("ContainedWithSecondaryLabelsAndIcons"),
        carbon_dash.Tabs(children=[carbon_dash.TabList(contained=True, children=[carbon_dash.Tab(renderIcon=dash_iconify.DashIconify(icon="carbon:task"), secondaryLabel='(21/25', children='Engage'), carbon_dash.Tab(renderIcon=dash_iconify.DashIconify(icon="carbon:ibm-watson-discovery"), secondaryLabel='(12/16)', children='Analyze'), carbon_dash.Tab(renderIcon=dash_iconify.DashIconify(icon="carbon:restart"), disabled=True, secondaryLabel='(0/7)', children='Remediate'), carbon_dash.Tab(renderIcon=dash_iconify.DashIconify(icon="carbon:dashboard"), secondaryLabel='(4/12)', children='Assets'), carbon_dash.Tab(renderIcon=dash_iconify.DashIconify(icon="carbon:cloud-monitoring"), secondaryLabel='(1/23)', children='Monitoring')]), carbon_dash.TabPanels(children=[carbon_dash.TabPanel(children='Tab Panel 1'), carbon_dash.TabPanel(children=carbon_dash.Layer()), carbon_dash.TabPanel(children='Tab Panel 3'), carbon_dash.TabPanel(children='Tab Panel 4'), carbon_dash.TabPanel(children='Tab Panel 5')])]),
        html.H3("ContainedFullWidth"),
        carbon_dash.Grid(condensed=True, children=carbon_dash.Column(lg=16, md=8, sm=4, children=carbon_dash.Tabs(children=[carbon_dash.TabList(contained=True, fullWidth=True, children=[carbon_dash.Tab(children='TLS'), carbon_dash.Tab(children='Origin'), carbon_dash.Tab(disabled=True, children='Rate limiting'), carbon_dash.Tab(children='WAF'), carbon_dash.Tab(children='IP Firewall'), carbon_dash.Tab(children='Firewall rules'), carbon_dash.Tab(children='Range'), carbon_dash.Tab(children='Mutual TLS')]), carbon_dash.TabPanels(children=[carbon_dash.TabPanel(children='Tab Panel 1'), carbon_dash.TabPanel(children=carbon_dash.Layer()), carbon_dash.TabPanel(children='Tab Panel 3'), carbon_dash.TabPanel(children='Tab Panel 4'), carbon_dash.TabPanel(children='Tab Panel 5'), carbon_dash.TabPanel(children='Tab Panel 6'), carbon_dash.TabPanel(children='Tab Panel 7'), carbon_dash.TabPanel(children='Tab Panel 8')])]))),
        html.H3("Vertical"),
        carbon_dash.TabsVertical(children=[carbon_dash.TabListVertical(children=[carbon_dash.Tab(children='Dashboard'), carbon_dash.Tab(children='Extra long label that will go two lines then truncate when it goes\n          beyond the Tab length'), carbon_dash.Tab(children='Activity'), carbon_dash.Tab(children='Analyze'), carbon_dash.Tab(children='Investigate'), carbon_dash.Tab(children='Learn'), carbon_dash.Tab(disabled=True, children='Settings')]), carbon_dash.TabPanels(children=[carbon_dash.TabPanel(children='Tab Panel 1'), carbon_dash.TabPanel(children=carbon_dash.Layer()), carbon_dash.TabPanel(children='Tab Panel 3'), carbon_dash.TabPanel(children='Tab Panel 4'), carbon_dash.TabPanel(children='Tab Panel 5'), carbon_dash.TabPanel(children='Tab Panel 6'), carbon_dash.TabPanel(children='Tab Panel 7')])]),
        html.H3("Skeleton"),
        carbon_dash.Tabs(id='tabs-skeleton'),
        html.H3("Icon20OnlyVisualSnapshots"),
        carbon_dash.Tabs(children=[carbon_dash.TabList(iconSize='lg', children=[carbon_dash.IconTab(label='Analyze', children=dash_iconify.DashIconify(icon="carbon:ibm-watson-discovery")), carbon_dash.IconTab(label='Activity', children=dash_iconify.DashIconify(icon="carbon:activity")), carbon_dash.IconTab(label='New Notifications', children=dash_iconify.DashIconify(icon="carbon:notification")), carbon_dash.IconTab(label='Chat', children=dash_iconify.DashIconify(icon="carbon:chat"))]), carbon_dash.TabPanels(children=[carbon_dash.TabPanel(children='Tab Panel 1'), carbon_dash.TabPanel(children='Tab Panel 2'), carbon_dash.TabPanel(children='Tab Panel 3'), carbon_dash.TabPanel(children='Tab Panel 4')])]),
        html.H3("IconOnlyVisualSnapshots"),
        carbon_dash.Tabs(children=[carbon_dash.TabList(iconSize='default', children=[carbon_dash.IconTab(label='Analyze', children=dash_iconify.DashIconify(icon="carbon:ibm-watson-discovery")), carbon_dash.IconTab(label='Activity', children=dash_iconify.DashIconify(icon="carbon:activity")), carbon_dash.IconTab(label='New Notifications', children=dash_iconify.DashIconify(icon="carbon:notification")), carbon_dash.IconTab(label='Chat', children=dash_iconify.DashIconify(icon="carbon:chat"))]), carbon_dash.TabPanels(children=[carbon_dash.TabPanel(children='Tab Panel 1'), carbon_dash.TabPanel(children='Tab Panel 2'), carbon_dash.TabPanel(children='Tab Panel 3'), carbon_dash.TabPanel(children='Tab Panel 4')])]),
    ])

stories_dict['node-tag'] = html.Div([
        html.H2("Tag"),
        html.H3("Selectable"),
        carbon_dash.Tag(disabled=False, id='tag-selectable'),
        html.H3("Operational"),
        carbon_dash.Tag(disabled=False, size='md', id='tag-operational'),
        html.H3("Dismissible"),
        carbon_dash.Tag(disabled=False, size='md', id='tag-dismissible'),
        html.H3("ReadOnly"),
        carbon_dash.Tag(disabled=False, filter=False, size='md', title='Clear filter', id='tag-readonly'),
        html.H3("Skeleton"),
        carbon_dash.Tag(size='md', id='tag-skeleton'),
        html.H3("withAILabel"),
        carbon_dash.Tag(disabled=False, size='md', id='tag-withailabel'),
    ])

stories_dict['node-textarea'] = html.Div([
        html.H2("TextArea"),
        html.H3("Default"),
        carbon_dash.TextArea(enableCounter=True, id='textarea-default'),
        html.H3("_WithLayer"),
        carbon_dash.TextArea(helperText='Optional helper text', id='textarea-_withlayer'),
        html.H3("withAILabel"),
        carbon_dash.TextArea(labelText='Text Area label', helperText='Optional helper text', rows=4, id='text-area-5'),
        html.H3("Skeleton"),
        carbon_dash.TextAreaSkeleton(),
    ])

stories_dict['node-textinput'] = html.Div([
        html.H2("TextInput"),
        html.H3("Default"),
        carbon_dash.TextInput(className='input-test-class', placeholder='Placeholder text', invalid=False, invalidText='Error message goes here', disabled=False, labelText='Label text', helperText='Helper text', warn=False, warnText='Warning message that is really long can wrap to more lines but should not be excessively long.', size='md', id='textinput-default'),
        html.H3("Fluid"),
        carbon_dash.TextInput(id='textinput-fluid'),
        html.H3("ReadOnly"),
        carbon_dash.TextInput(defaultValue='This is read only, you can\'t type more.', readOnly=True, id='textinput-readonly'),
        html.H3("_WithLayer"),
        carbon_dash.TextInput(id='textinput-_withlayer'),
        html.H3("withAILabel"),
        carbon_dash.TextInput(id='textinput-withailabel'),
        html.H3("Skeleton"),
        carbon_dash.TextInputSkeleton(hideLabel=False),
        html.H3("TestInvalidTextNoOverlap"),
        carbon_dash.TextInput(id='textinput-testinvalidtextnooverlap'),
    ])

stories_dict['node-theme'] = html.Div([
        html.H2("Theme"),
        html.H3("UseTheme"),
        carbon_dash.Theme(id='theme-usetheme'),
        html.H3("UsePrefersDarkScheme"),
        carbon_dash.Theme(children=[carbon_dash.Theme(), carbon_dash.Theme(), carbon_dash.Theme()]),
        html.H3("_WithLayer"),
        carbon_dash.VStack(gap=7),
    ])

stories_dict['node-tile'] = html.Div([
        html.H2("Tile"),
        html.H3("Clickable"),
        carbon_dash.ClickableTile(id='clickable-tile-1', href='https://www.carbondesignsystem.com/', children='Clickable Tile'),
        html.H3("ClickableWithLayer"),
        carbon_dash.Tile(id='tile-clickablewithlayer'),
        html.H3("Selectable"),
        carbon_dash.SelectableTile(id='selectable-tile-1', children='Selectable'),
        html.H3("MultiSelect"),
        carbon_dash.Tile(id='tile-multiselect'),
        html.H3("Radio"),
        carbon_dash.TileGroup(defaultSelected='default-selected', legend='Radio Tile Group', name='radio tile group', children=[carbon_dash.RadioTile(id='radio-tile-1', value='standard', children='Option 1'), carbon_dash.RadioTile(id='radio-tile-2', value='default-selected', children='Option 2'), carbon_dash.RadioTile(id='radio-tile-3', value='selected', children='Option 3')]),
        html.H3("RadioWithLayer"),
        carbon_dash.Tile(id='tile-radiowithlayer'),
        html.H3("Expandable"),
        carbon_dash.Tile(id='tile-expandable'),
        html.H3("ExpandableWithInteractive"),
        carbon_dash.Tile(id='tile-expandablewithinteractive'),
        html.H3("ExpandableWithLayer"),
        carbon_dash.Tile(id='tile-expandablewithlayer'),
        html.H3("_WithAILabel"),
        carbon_dash.Tile(id='tile-_withailabel'),
        html.H3("DefaultWithLayer"),
        carbon_dash.Tile(id='tile-defaultwithlayer'),
        html.H3("ClickableWithCustomIcon"),
        carbon_dash.ClickableTile(id='clickable-tile-1', href='https://www.carbondesignsystem.com/', renderIcon=dash_iconify.DashIconify(icon="carbon:launch"), children='Clickable Tile'),
        html.H3("withAILabel"),
        carbon_dash.Tile(id='tile-withailabel'),
    ])

stories_dict['node-timepicker'] = html.Div([
        html.H2("TimePicker"),
        html.H3("Default"),
        carbon_dash.TimePicker(disabled=False, hideLabel=False, invalid=False, warning=False, id='timepicker-default'),
        html.H3("_WithLayer"),
        carbon_dash.TimePicker(id='timepicker-_withlayer'),
    ])

stories_dict['node-toggle'] = html.Div([
        html.H2("Toggle"),
        html.H3("_Toggle"),
        carbon_dash.Toggle(disabled=False, id='toggle-_toggle'),
        html.H3("SmallToggle"),
        carbon_dash.Toggle(size='sm', labelText='Label', labelA='Off', labelB='On', defaultToggled=True, id='toggle-2'),
        html.H3("WithAccessibleLabels"),
        carbon_dash.VStack(gap=7, children=[carbon_dash.Toggle(id='toggle-4', labelText='Label'), carbon_dash.Toggle(id='toggle-5', labelText='Label', hideLabel=True)]),
        html.H3("Skeleton"),
        carbon_dash.Toggle(id='toggle-skeleton'),
    ])

stories_dict['node-toggletip'] = html.Div([
        html.H2("Toggletip"),
        html.H3("FloatingStyles"),
        carbon_dash.Toggletip(align='bottom', id='toggletip-floatingstyles'),
        html.H3("ExperimentalAutoAlign"),
        carbon_dash.Toggletip(id='toggletip-experimentalautoalign'),
    ])

stories_dict['node-tooltip'] = html.Div([
        html.H2("Tooltip"),
        html.H3("Default"),
        carbon_dash.Tooltip(align='bottom-left', defaultOpen=False, id='tooltip-default'),
        html.H3("WithLargeText"),
        carbon_dash.Tooltip(align='bottom-left', defaultOpen=False, id='tooltip-withlargetext'),
        html.H3("FloatingStyles"),
        carbon_dash.Tooltip(align='bottom', id='tooltip-floatingstyles'),
        html.H3("Alignment"),
        carbon_dash.Tooltip(label='Tooltip alignment', align='bottom-left', children=carbon_dash.Button(children='This button has a tooltip')),
        html.H3("ExperimentalAutoAlign"),
        carbon_dash.Tooltip(id='tooltip-experimentalautoalign'),
        html.H3("Duration"),
        carbon_dash.Tooltip(label='Label one', enterDelayMs=0, leaveDelayMs=300, children=carbon_dash.Button(children='This button has a tooltip')),
    ])

stories_dict['node-treeview'] = html.Div([
        html.H2("TreeView"),
        html.H3("Default"),
        carbon_dash.TreeView(hideLabel=False, multiselect=False, id='treeview-default'),
        html.H3("WithIcons"),
        carbon_dash.TreeView(label='Tree View'),
        html.H3("WithLinks"),
        carbon_dash.TreeView(id='treeview-withlinks'),
        html.H3("WithControlledExpansion"),
        carbon_dash.TreeView(id='treeview-withcontrolledexpansion'),
        html.H3("WithComplexNesting"),
        carbon_dash.TreeView(label='Tree View with Complex Nesting', children=[carbon_dash.TreeNode(id='1', value='A.I.', label='A.I.', isExpanded=True, children=carbon_dash.TreeNode(id='1-2', value='Sub 2', label='Sub 2 (direct child)', children=carbon_dash.TreeNode(id='1-2-1', value='Sub 2.1', label='Sub 2.1'))), carbon_dash.TreeNode(id='2', value='Analytics', label='Analytics', isExpanded=True), carbon_dash.TreeNode(id='3', value='Trust', label='Trust')], hideLabel=True, multiselect=True),
    ])

stories_dict['node-unorderedlist'] = html.Div([
        html.H2("UnorderedList"),
        html.H3("Default"),
        carbon_dash.UnorderedList(isExpressive=False, id='unorderedlist-default'),
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
                            id='node-formgroup',
                            label='FormGroup',
                            value='FormGroup'
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
                            id='node-loading',
                            label='Loading',
                            value='Loading'
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
                            id='node-paginationnav',
                            label='PaginationNav',
                            value='PaginationNav'
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
                            id='node-skeletontext',
                            label='SkeletonText',
                            value='SkeletonText'
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
