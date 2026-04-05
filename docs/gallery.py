import os
import sys

# Add root directory to sys.path to ensure carbon_dash can be imported
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

import carbon_dash
from dash import Dash, html, dcc

app = Dash(__name__)

app.layout = html.Div([
    html.H1("Carbon Dash Component Gallery"),
    html.Div([
        html.Section([
            html.H3("Button"),
            html.Div([
                carbon_dash.Button(
                    id='gallery-button-primary',
                    children='Primary Button',
                    kind='primary',
                    style={'margin-right': '10px'}
                ),
                carbon_dash.Button(
                    id='gallery-button-secondary',
                    children='Secondary Button',
                    kind='secondary',
                    style={'margin-right': '10px'}
                ),
                carbon_dash.Button(
                    id='gallery-button-danger',
                    children='Danger Button',
                    kind='danger',
                    style={'margin-right': '10px'}
                ),
                carbon_dash.Button(
                    id='gallery-button-ghost',
                    children='Ghost Button',
                    kind='ghost',
                    style={'margin-right': '10px'}
                ),
                carbon_dash.Button(
                    id='gallery-button-disabled',
                    children='Disabled Button',
                    disabled=True
                ),
            ], style={'display': 'flex', 'flex-wrap': 'wrap', 'gap': '10px'}),
            html.Hr()
        ], style={'padding': '20px'}),

        html.Section([
            html.H3("Checkbox"),
            carbon_dash.Checkbox(
                id='gallery-checkbox',
                
                
                label='Checkbox',
                
            ),
            html.Hr()
        ], style={'padding': '20px'}),

        html.Section([
            html.H3("TextInput"),
            carbon_dash.TextInput(
                id='gallery-textinput',
                
                
                
                label='Text Input',
            ),
            html.Hr()
        ], style={'padding': '20px'}),

        html.Section([
            html.H3("Toggle"),
            carbon_dash.Toggle(
                id='gallery-toggle',
                
                
                
                
            ),
            html.Hr()
        ], style={'padding': '20px'}),

        html.Section([
            html.H3("Dropdown"),
            carbon_dash.Dropdown(
                id='gallery-dropdown',
                
                items=['Option 1', 'Option 2'],
                
                
            ),
            html.Hr()
        ], style={'padding': '20px'}),

        html.Section([
            html.H3("Slider"),
            carbon_dash.Slider(
                id='gallery-slider',
                label='Slider Example',
                value=50,
                min=0,
                max=100,
                step=1,
            ),
            html.Hr()
        ], style={'padding': '20px'}),

        html.Section([
            html.H3("NumberInput"),
            carbon_dash.NumberInput(
                id='gallery-numberinput',
                
                
                
                
            ),
            html.Hr()
        ], style={'padding': '20px'}),

        html.Section([
            html.H3("TextArea"),
            carbon_dash.TextArea(
                id='gallery-textarea',
                
                
                
                
            ),
            html.Hr()
        ], style={'padding': '20px'}),

        html.Section([
            html.H3("Select"),
            carbon_dash.Select(
                id='gallery-select',
                
                
                
                
            ),
            html.Hr()
        ], style={'padding': '20px'}),

        html.Section([
            html.H3("RadioButton"),
            carbon_dash.RadioButton(
                id='gallery-radiobutton',
                
                
                
                
            ),
            html.Hr()
        ], style={'padding': '20px'}),

        html.Section([
            html.H3("RadioButtonGroup"),
            carbon_dash.RadioButtonGroup(
                id='gallery-radiobuttongroup',
                
                
                
                
            ),
            html.Hr()
        ], style={'padding': '20px'}),

        html.Section([
            html.H3("Grid"),
            carbon_dash.Grid(
                id='gallery-grid',
                
                
                
                
            ),
            html.Hr()
        ], style={'padding': '20px'}),

        html.Section([
            html.H3("Row"),
            carbon_dash.Row(
                id='gallery-row',
                
                
                
                
            ),
            html.Hr()
        ], style={'padding': '20px'}),

        html.Section([
            html.H3("Column"),
            carbon_dash.Column(
                id='gallery-column',
                
                
                
                
            ),
            html.Hr()
        ], style={'padding': '20px'}),

        html.Section([
            html.H3("Accordion"),
            carbon_dash.Accordion(
                id='gallery-accordion',
                
                
                
                
            ),
            html.Hr()
        ], style={'padding': '20px'}),

        html.Section([
            html.H3("AccordionItem"),
            carbon_dash.AccordionItem(
                id='gallery-accordionitem',
                
                
                
                
            ),
            html.Hr()
        ], style={'padding': '20px'}),

        html.Section([
            html.H3("Tabs"),
            carbon_dash.Tabs(
                id='gallery-tabs',
                
                
                
                
            ),
            html.Hr()
        ], style={'padding': '20px'}),

        html.Section([
            html.H3("TabList"),
            carbon_dash.TabList(
                id='gallery-tablist',
                
                
                
                
            ),
            html.Hr()
        ], style={'padding': '20px'}),

        html.Section([
            html.H3("Tab"),
            carbon_dash.Tab(
                id='gallery-tab',
                
                
                
                
            ),
            html.Hr()
        ], style={'padding': '20px'}),

        html.Section([
            html.H3("TabPanels"),
            carbon_dash.TabPanels(
                id='gallery-tabpanels',
                
                
                
                
            ),
            html.Hr()
        ], style={'padding': '20px'}),

        html.Section([
            html.H3("TabPanel"),
            carbon_dash.TabPanel(
                id='gallery-tabpanel',
                
                
                
                
            ),
            html.Hr()
        ], style={'padding': '20px'}),

        html.Section([
            html.H3("Modal"),
            carbon_dash.Modal(
                id='gallery-modal',
                
                
                
                
            ),
            html.Hr()
        ], style={'padding': '20px'}),

        html.Section([
            html.H3("Loading"),
            carbon_dash.Loading(
                id='gallery-loading',
                
                
                
                
            ),
            html.Hr()
        ], style={'padding': '20px'}),

        html.Section([
            html.H3("Breadcrumb"),
            carbon_dash.Breadcrumb(
                id='gallery-breadcrumb',
                
                
                
                
            ),
            html.Hr()
        ], style={'padding': '20px'}),

        html.Section([
            html.H3("BreadcrumbItem"),
            carbon_dash.BreadcrumbItem(
                id='gallery-breadcrumbitem',
                
                
                
                
            ),
            html.Hr()
        ], style={'padding': '20px'}),

        html.Section([
            html.H3("Tag"),
            carbon_dash.Tag(
                id='gallery-tag',
                
                
                
                
            ),
            html.Hr()
        ], style={'padding': '20px'}),

        html.Section([
            html.H3("Tooltip"),
            carbon_dash.Tooltip(
                id='gallery-tooltip',
                
                
                
                
            ),
            html.Hr()
        ], style={'padding': '20px'}),

        html.Section([
            html.H3("ProgressIndicator"),
            carbon_dash.ProgressIndicator(
                id='gallery-progressindicator',
                
                
                
                
            ),
            html.Hr()
        ], style={'padding': '20px'}),

        html.Section([
            html.H3("ProgressStep"),
            carbon_dash.ProgressStep(
                id='gallery-progressstep',
                
                
                
                
            ),
            html.Hr()
        ], style={'padding': '20px'}),

        html.Section([
            html.H3("AILabel"),
            carbon_dash.AILabel(
                id='gallery-ailabel',
                
                
                
                
            ),
            html.Hr()
        ], style={'padding': '20px'}),

        html.Section([
            html.H3("AISkeletonIcon"),
            carbon_dash.AISkeletonIcon(
                id='gallery-aiskeletonicon',
            ),
            html.Hr()
        ], style={'padding': '20px'}),

        html.Section([
            html.H3("AISkeletonPlaceholder"),
            carbon_dash.AISkeletonPlaceholder(
                id='gallery-aiskeletonplaceholder',
            ),
            html.Hr()
        ], style={'padding': '20px'}),

        html.Section([
            html.H3("AISkeletonText"),
            carbon_dash.AISkeletonText(
                id='gallery-aiskeletontext',
            ),
            html.Hr()
        ], style={'padding': '20px'}),

        html.Section([
            html.H3("AspectRatio"),
            carbon_dash.AspectRatio(
                id='gallery-aspectratio',
                
                
                
                
            ),
            html.Hr()
        ], style={'padding': '20px'}),

        # html.Section([
        #     html.H3("BadgeIndicator"),
        #     carbon_dash.BadgeIndicator(
        #         id='gallery-badgeindicator',
        #         
        #         
        #         
        #         
        #     ),
        #     html.Hr()
        # ], style={'padding': '20px'}),

        html.Section([
            html.H3("ButtonSet"),
            carbon_dash.ButtonSet(
                id='gallery-buttonset',
                
                
                
                
            ),
            html.Hr()
        ], style={'padding': '20px'}),

        # html.Section([
        #     html.H3("ChatButton"),
        #     carbon_dash.ChatButton(
        #         id='gallery-chatbutton',
        #         
        #         
        #         
        #         
        #     ),
        #     html.Hr()
        # ], style={'padding': '20px'}),

        html.Section([
            html.H3("CheckboxGroup"),
            carbon_dash.CheckboxGroup(
                id='gallery-checkboxgroup',
                
                
                
                
            ),
            html.Hr()
        ], style={'padding': '20px'}),

        html.Section([
            html.H3("ClassPrefix"),
            carbon_dash.ClassPrefix(
                id='gallery-classprefix',
                
                
                
                
            ),
            html.Hr()
        ], style={'padding': '20px'}),

        html.Section([
            html.H3("CodeSnippet"),
            carbon_dash.CodeSnippet(
                id='gallery-codesnippet',
                
                
                
                
            ),
            html.Hr()
        ], style={'padding': '20px'}),

        html.Section([
            html.H3("ComboBox"),
            carbon_dash.ComboBox(
                id='gallery-combobox',
                
                
                
                
            ),
            html.Hr()
        ], style={'padding': '20px'}),

        html.Section([
            html.H3("ComboButton"),
            carbon_dash.ComboButton(
                id='gallery-combobutton',
                
                
                
                
            ),
            html.Hr()
        ], style={'padding': '20px'}),

        html.Section([
            html.H3("ComposedModal"),
            carbon_dash.ComposedModal(
                id='gallery-composedmodal',
                
                
                
                
            ),
            html.Hr()
        ], style={'padding': '20px'}),

        html.Section([
            html.H3("ContainedList"),
            carbon_dash.ContainedList(
                id='gallery-containedlist',
                
                
                
                
            ),
            html.Hr()
        ], style={'padding': '20px'}),

        html.Section([
            html.H3("ContentSwitcher"),
            carbon_dash.ContentSwitcher(
                id='gallery-contentswitcher',
                
                
                
                
            ),
            html.Hr()
        ], style={'padding': '20px'}),

        html.Section([
            html.H3("ContextMenu"),
            carbon_dash.ContextMenu(
                id='gallery-contextmenu',
                
                
                
                
            ),
            html.Hr()
        ], style={'padding': '20px'}),

        html.Section([
            html.H3("Copy"),
            carbon_dash.Copy(
                id='gallery-copy',
                
                
                
                
            ),
            html.Hr()
        ], style={'padding': '20px'}),

        html.Section([
            html.H3("CopyButton"),
            carbon_dash.CopyButton(
                id='gallery-copybutton',
                
                
                
                
            ),
            html.Hr()
        ], style={'padding': '20px'}),

        html.Section([
            html.H3("DangerButton"),
            carbon_dash.DangerButton(
                id='gallery-dangerbutton',
                
                
                
                
            ),
            html.Hr()
        ], style={'padding': '20px'}),

        html.Section([
            html.H3("DataTable"),
            html.Div([
                html.H4("Basic DataTable"),
                carbon_dash.DataTable(
                    id='gallery-datatable-basic',
                    headers=[
                        {'key': 'name', 'header': 'Name'},
                        {'key': 'protocol', 'header': 'Protocol'},
                        {'key': 'port', 'header': 'Port'},
                        {'key': 'rule', 'header': 'Rule'},
                    ],
                    rows=[
                        {'id': 'a', 'name': 'Load Balancer 1', 'protocol': 'HTTP', 'port': 80, 'rule': 'Round Robin'},
                        {'id': 'b', 'name': 'Load Balancer 2', 'protocol': 'HTTP', 'port': 80, 'rule': 'DNS LBAAS'},
                        {'id': 'c', 'name': 'Load Balancer 3', 'protocol': 'HTTP', 'port': 8080, 'rule': 'Round Robin'},
                    ],
                    title='DataTable',
                    description='A basic data table.'
                ),
                html.Br(),
                html.H4("Zebra Styles + Selection DataTable"),
                carbon_dash.DataTable(
                    id='gallery-datatable-selection',
                    headers=[
                        {'key': 'name', 'header': 'Name'},
                        {'key': 'status', 'header': 'Status'},
                    ],
                    rows=[
                        {'id': '1', 'name': 'Component 1', 'status': 'Active'},
                        {'id': '2', 'name': 'Component 2', 'status': 'Inactive'},
                        {'id': '3', 'name': 'Component 3', 'status': 'Active'},
                    ],
                    useZebraStyles=True,
                    withSelection=True,
                    title='Zebra + Selection',
                ),
                html.Br(),
                html.H4("Compact + Sortable DataTable"),
                carbon_dash.DataTable(
                    id='gallery-datatable-sortable',
                    headers=[
                        {'key': 'name', 'header': 'Name'},
                        {'key': 'value', 'header': 'Value'},
                    ],
                    rows=[
                        {'id': 'x', 'name': 'Metric X', 'value': '100'},
                        {'id': 'y', 'name': 'Metric Y', 'value': '200'},
                        {'id': 'z', 'name': 'Metric Z', 'value': '150'},
                    ],
                    size='sm',
                    isSortable=True,
                    title='Compact + Sortable',
                ),
                html.Br(),
                html.H4("Expansion DataTable"),
                carbon_dash.DataTable(
                    id='gallery-datatable-expansion',
                    headers=[
                        {'key': 'name', 'header': 'Name'},
                        {'key': 'description', 'header': 'Description'},
                    ],
                    rows=[
                        {'id': 'exp1', 'name': 'Row 1', 'description': 'Main content'},
                        {'id': 'exp2', 'name': 'Row 2', 'description': 'Main content'},
                    ],
                    withExpansion=True,
                    title='With Expansion',
                ),
            ]),
            html.Hr()
        ], style={'padding': '20px'}),

        html.Section([
            html.H3("DataTableSkeleton"),
            carbon_dash.DataTableSkeleton(
                id='gallery-datatableskeleton',
                
                
                
                
            ),
            html.Hr()
        ], style={'padding': '20px'}),

        html.Section([
            html.H3("DatePicker"),
            carbon_dash.DatePicker(
                id='gallery-datepicker',
                
                
                
                
            ),
            html.Hr()
        ], style={'padding': '20px'}),

        html.Section([
            html.H3("DatePickerInput"),
            carbon_dash.DatePickerInput(
                id='gallery-datepickerinput',
                
                
                
                
            ),
            html.Hr()
        ], style={'padding': '20px'}),

        html.Section([
            html.H3("Dialog"),
            carbon_dash.Dialog(
                id='gallery-dialog',
                
                
                
                
            ),
            html.Hr()
        ], style={'padding': '20px'}),

        html.Section([
            html.H3("Disclosure"),
            carbon_dash.Disclosure(
                id='gallery-disclosure',
                
                
                
                
            ),
            html.Hr()
        ], style={'padding': '20px'}),

        html.Section([
            html.H3("ErrorBoundary"),
            carbon_dash.ErrorBoundary(
                id='gallery-errorboundary',
                
                
                
                
            ),
            html.Hr()
        ], style={'padding': '20px'}),

        html.Section([
            html.H3("ExpandableSearch"),
            carbon_dash.ExpandableSearch(
                id='gallery-expandablesearch',
                
                
                
                
            ),
            html.Hr()
        ], style={'padding': '20px'}),

        html.Section([
            html.H3("FeatureFlags"),
            carbon_dash.FeatureFlags(
                id='gallery-featureflags',
                
                
                
                
            ),
            html.Hr()
        ], style={'padding': '20px'}),

        html.Section([
            html.H3("FileUploader"),
            carbon_dash.FileUploader(
                id='gallery-fileuploader',
                
                
                
                
            ),
            html.Hr()
        ], style={'padding': '20px'}),

        html.Section([
            html.H3("FlexGrid"),
            carbon_dash.FlexGrid(
                id='gallery-flexgrid',
                
                
                
                
            ),
            html.Hr()
        ], style={'padding': '20px'}),

        html.Section([
            html.H3("FluidComboBox"),
            carbon_dash.FluidComboBox(
                id='gallery-fluidcombobox',
                
                
                
                
            ),
            html.Hr()
        ], style={'padding': '20px'}),

        html.Section([
            html.H3("FluidDatePicker"),
            carbon_dash.FluidDatePicker(
                id='gallery-fluiddatepicker',
                
                
                
                
            ),
            html.Hr()
        ], style={'padding': '20px'}),

        html.Section([
            html.H3("FluidDatePickerInput"),
            carbon_dash.FluidDatePickerInput(
                id='gallery-fluiddatepickerinput',
                
                
                
                
            ),
            html.Hr()
        ], style={'padding': '20px'}),

        html.Section([
            html.H3("FluidDropdown"),
            carbon_dash.FluidDropdown(
                id='gallery-fluiddropdown',
                
                
                
                
            ),
            html.Hr()
        ], style={'padding': '20px'}),

        html.Section([
            html.H3("FluidForm"),
            carbon_dash.FluidForm(
                id='gallery-fluidform',
                
                
                
                
            ),
            html.Hr()
        ], style={'padding': '20px'}),

        html.Section([
            html.H3("FluidMultiSelect"),
            carbon_dash.FluidMultiSelect(
                id='gallery-fluidmultiselect',
                
                
                
                
            ),
            html.Hr()
        ], style={'padding': '20px'}),

        html.Section([
            html.H3("FluidNumberInput"),
            carbon_dash.FluidNumberInput(
                id='gallery-fluidnumberinput',
                
                
                
                
            ),
            html.Hr()
        ], style={'padding': '20px'}),

        html.Section([
            html.H3("FluidSearch"),
            carbon_dash.FluidSearch(
                id='gallery-fluidsearch',
                
                
                
                
            ),
            html.Hr()
        ], style={'padding': '20px'}),

        html.Section([
            html.H3("FluidSelect"),
            carbon_dash.FluidSelect(
                id='gallery-fluidselect',
                
                
                
                
            ),
            html.Hr()
        ], style={'padding': '20px'}),

        html.Section([
            html.H3("FluidTextArea"),
            carbon_dash.FluidTextArea(
                id='gallery-fluidtextarea',
                
                
                
                
            ),
            html.Hr()
        ], style={'padding': '20px'}),

        html.Section([
            html.H3("FluidTextInput"),
            carbon_dash.FluidTextInput(
                id='gallery-fluidtextinput',
                
                
                
                
            ),
            html.Hr()
        ], style={'padding': '20px'}),

        html.Section([
            html.H3("FluidTimePicker"),
            carbon_dash.FluidTimePicker(
                id='gallery-fluidtimepicker',
                
                
                
                
            ),
            html.Hr()
        ], style={'padding': '20px'}),

        html.Section([
            html.H3("FluidTimePickerSelect"),
            carbon_dash.FluidTimePickerSelect(
                id='gallery-fluidtimepickerselect',
                
                
                
                
            ),
            html.Hr()
        ], style={'padding': '20px'}),

        html.Section([
            html.H3("Form"),
            carbon_dash.Form(
                id='gallery-form',
                
                
                
                
            ),
            html.Hr()
        ], style={'padding': '20px'}),

        html.Section([
            html.H3("FormGroup"),
            carbon_dash.FormGroup(
                id='gallery-formgroup',
                
                
                
                
            ),
            html.Hr()
        ], style={'padding': '20px'}),

        html.Section([
            html.H3("FormItem"),
            carbon_dash.FormItem(
                id='gallery-formitem',
                
                
                
                
            ),
            html.Hr()
        ], style={'padding': '20px'}),

        html.Section([
            html.H3("FormLabel"),
            carbon_dash.FormLabel(
                id='gallery-formlabel',
                
                
                
                
            ),
            html.Hr()
        ], style={'padding': '20px'}),

        html.Section([
            html.H3("Heading"),
            carbon_dash.Heading(
                id='gallery-heading',
                
                
                
                
            ),
            html.Hr()
        ], style={'padding': '20px'}),

        html.Section([
            html.H3("HideAtBreakpoint"),
            carbon_dash.HideAtBreakpoint(
                id='gallery-hideatbreakpoint',
                
                
                
                
            ),
            html.Hr()
        ], style={'padding': '20px'}),

        html.Section([
            html.H3("Icon"),
            carbon_dash.Icon(
                id='gallery-icon',
                
                
                
                
            ),
            html.Hr()
        ], style={'padding': '20px'}),

        html.Section([
            html.H3("IconButton"),
            carbon_dash.IconButton(
                id='gallery-iconbutton',
                
                
                
                
            ),
            html.Hr()
        ], style={'padding': '20px'}),

        html.Section([
            html.H3("IconIndicator"),
            carbon_dash.IconIndicator(
                id='gallery-iconindicator',
                
                
                
                
            ),
            html.Hr()
        ], style={'padding': '20px'}),

        html.Section([
            html.H3("Icons"),
            carbon_dash.Icons(
                id='gallery-icons',
                
                
                
                
            ),
            html.Hr()
        ], style={'padding': '20px'}),

        html.Section([
            html.H3("IdPrefix"),
            carbon_dash.IdPrefix(
                id='gallery-idprefix',
                
                
                
                
            ),
            html.Hr()
        ], style={'padding': '20px'}),

        html.Section([
            html.H3("InlineCheckbox"),
            carbon_dash.InlineCheckbox(
                id='gallery-inlinecheckbox',
                
                
                
                
            ),
            html.Hr()
        ], style={'padding': '20px'}),

        html.Section([
            html.H3("InlineLoading"),
            carbon_dash.InlineLoading(
                id='gallery-inlineloading',
                
                
                
                
            ),
            html.Hr()
        ], style={'padding': '20px'}),

        html.Section([
            html.H3("Layer"),
            carbon_dash.Layer(
                id='gallery-layer',
                
                
                
                
            ),
            html.Hr()
        ], style={'padding': '20px'}),

        html.Section([
            html.H3("Layout"),
            carbon_dash.Layout(
                id='gallery-layout',
                
                
                
                
            ),
            html.Hr()
        ], style={'padding': '20px'}),

        html.Section([
            html.H3("LayoutDirection"),
            carbon_dash.LayoutDirection(
                id='gallery-layoutdirection',
                
                
                
                
            ),
            html.Hr()
        ], style={'padding': '20px'}),

        html.Section([
            html.H3("Link"),
            carbon_dash.Link(
                id='gallery-link',
                
                
                
                
            ),
            html.Hr()
        ], style={'padding': '20px'}),

        html.Section([
            html.H3("ListBox"),
            carbon_dash.ListBox(
                id='gallery-listbox',
                
                
                
                
            ),
            html.Hr()
        ], style={'padding': '20px'}),

        html.Section([
            html.H3("ListItem"),
            carbon_dash.ListItem(
                id='gallery-listitem',
                
                
                
                
            ),
            html.Hr()
        ], style={'padding': '20px'}),

        html.Section([
            html.H3("Menu"),
            carbon_dash.Menu(
                id='gallery-menu',
                
                
                
                
            ),
            html.Hr()
        ], style={'padding': '20px'}),

        html.Section([
            html.H3("MenuButton"),
            carbon_dash.MenuButton(
                id='gallery-menubutton',
                
                
                
                
            ),
            html.Hr()
        ], style={'padding': '20px'}),

        html.Section([
            html.H3("ModalWrapper"),
            carbon_dash.ModalWrapper(
                id='gallery-modalwrapper',
                
                
                
                
            ),
            html.Hr()
        ], style={'padding': '20px'}),

        html.Section([
            html.H3("MultiSelect"),
            carbon_dash.MultiSelect(
                id='gallery-multiselect',
                
                
                
                
            ),
            html.Hr()
        ], style={'padding': '20px'}),

        html.Section([
            html.H3("Notification"),
            carbon_dash.Notification(
                id='gallery-notification',
                
                
                
                
            ),
            html.Hr()
        ], style={'padding': '20px'}),

        html.Section([
            html.H3("OrderedList"),
            carbon_dash.OrderedList(
                id='gallery-orderedlist',
                
                
                
                
            ),
            html.Hr()
        ], style={'padding': '20px'}),

        html.Section([
            html.H3("OverflowMenu"),
            carbon_dash.OverflowMenu(
                id='gallery-overflowmenu',
                
                
                
                
            ),
            html.Hr()
        ], style={'padding': '20px'}),

        html.Section([
            html.H3("OverflowMenuItem"),
            carbon_dash.OverflowMenuItem(
                id='gallery-overflowmenuitem',
                
                
                
                
            ),
            html.Hr()
        ], style={'padding': '20px'}),

        html.Section([
            html.H3("OverflowMenuV2"),
            carbon_dash.OverflowMenuV2(
                id='gallery-overflowmenuv2',
                
                
                
                
            ),
            html.Hr()
        ], style={'padding': '20px'}),

        html.Section([
            html.H3("PageHeader"),
            carbon_dash.PageHeader(
                id='gallery-pageheader',
                
                
                
                
            ),
            html.Hr()
        ], style={'padding': '20px'}),

        html.Section([
            html.H3("Pagination"),
            carbon_dash.Pagination(
                id='gallery-pagination',
                
                
                
                
            ),
            html.Hr()
        ], style={'padding': '20px'}),

        html.Section([
            html.H3("PaginationNav"),
            carbon_dash.PaginationNav(
                id='gallery-paginationnav',
                
                
                
                
            ),
            html.Hr()
        ], style={'padding': '20px'}),

        html.Section([
            html.H3("PasswordInput"),
            carbon_dash.PasswordInput(
                id='gallery-passwordinput',
                
                
                
                
            ),
            html.Hr()
        ], style={'padding': '20px'}),

        html.Section([
            html.H3("Plex"),
            carbon_dash.Plex(
                id='gallery-plex',
                
                
                
                
            ),
            html.Hr()
        ], style={'padding': '20px'}),

        html.Section([
            html.H3("Popover"),
            carbon_dash.Popover(
                id='gallery-popover',
                
                
                
                
            ),
            html.Hr()
        ], style={'padding': '20px'}),

        html.Section([
            html.H3("Portal"),
            carbon_dash.Portal(
                id='gallery-portal',
                
                
                
                
            ),
            html.Hr()
        ], style={'padding': '20px'}),

        html.Section([
            html.H3("PrimaryButton"),
            carbon_dash.PrimaryButton(
                id='gallery-primarybutton',
                
                
                
                
            ),
            html.Hr()
        ], style={'padding': '20px'}),

        html.Section([
            html.H3("ProgressBar"),
            carbon_dash.ProgressBar(
                id='gallery-progressbar',
                
                
                
                
            ),
            html.Hr()
        ], style={'padding': '20px'}),

        html.Section([
            html.H3("RadioTile"),
            carbon_dash.RadioTile(
                id='gallery-radiotile',
                
                
                
                
            ),
            html.Hr()
        ], style={'padding': '20px'}),

        html.Section([
            html.H3("Search"),
            carbon_dash.Search(
                id='gallery-search',
                
                
                
                
            ),
            html.Hr()
        ], style={'padding': '20px'}),

        html.Section([
            html.H3("SecondaryButton"),
            carbon_dash.SecondaryButton(
                id='gallery-secondarybutton',
                
                
                
                
            ),
            html.Hr()
        ], style={'padding': '20px'}),

        html.Section([
            html.H3("SelectItemGroup"),
            carbon_dash.SelectItemGroup(
                id='gallery-selectitemgroup',
                
                
                
                
            ),
            html.Hr()
        ], style={'padding': '20px'}),

        html.Section([
            html.H3("ShapeIndicator"),
            carbon_dash.ShapeIndicator(
                id='gallery-shapeindicator',
                
                
                
                
            ),
            html.Hr()
        ], style={'padding': '20px'}),

        html.Section([
            html.H3("SkeletonIcon"),
            carbon_dash.SkeletonIcon(
                id='gallery-skeletonicon',
                
                
                
                
            ),
            html.Hr()
        ], style={'padding': '20px'}),

        html.Section([
            html.H3("SkeletonPlaceholder"),
            carbon_dash.SkeletonPlaceholder(
                id='gallery-skeletonplaceholder',
                
                
                
                
            ),
            html.Hr()
        ], style={'padding': '20px'}),

        html.Section([
            html.H3("SkeletonText"),
            carbon_dash.SkeletonText(
                id='gallery-skeletontext',
                
                
                
                
            ),
            html.Hr()
        ], style={'padding': '20px'}),

        html.Section([
            html.H3("Stack"),
            carbon_dash.Stack(
                id='gallery-stack',
                
                
                
                
            ),
            html.Hr()
        ], style={'padding': '20px'}),

        html.Section([
            html.H3("StructuredList"),
            carbon_dash.StructuredList(
                id='gallery-structuredlist',
                
                
                
                
            ),
            html.Hr()
        ], style={'padding': '20px'}),

        html.Section([
            html.H3("Switch"),
            carbon_dash.Switch(
                id='gallery-switch',
                
                
                
                
            ),
            html.Hr()
        ], style={'padding': '20px'}),

        html.Section([
            html.H3("TabContent"),
            carbon_dash.TabContent(
                id='gallery-tabcontent',
                
                
                
                
            ),
            html.Hr()
        ], style={'padding': '20px'}),

        html.Section([
            html.H3("Text"),
            carbon_dash.Text(
                id='gallery-text',
                
                
                
                
            ),
            html.Hr()
        ], style={'padding': '20px'}),

        html.Section([
            html.H3("Theme"),
            carbon_dash.Theme(
                id='gallery-theme',
                
                
                
                
            ),
            html.Hr()
        ], style={'padding': '20px'}),

        html.Section([
            html.H3("Tile"),
            carbon_dash.Tile(
                id='gallery-tile',
                
                
                
                
            ),
            html.Hr()
        ], style={'padding': '20px'}),

        html.Section([
            html.H3("TileGroup"),
            carbon_dash.TileGroup(
                id='gallery-tilegroup',
                
                
                
                
            ),
            html.Hr()
        ], style={'padding': '20px'}),

        html.Section([
            html.H3("TimePicker"),
            carbon_dash.TimePicker(
                id='gallery-timepicker',
                
                
                
                
            ),
            html.Hr()
        ], style={'padding': '20px'}),

        html.Section([
            html.H3("TimePickerSelect"),
            carbon_dash.TimePickerSelect(
                id='gallery-timepickerselect',
                
                
                
                
            ),
            html.Hr()
        ], style={'padding': '20px'}),

        html.Section([
            html.H3("ToggleSmall"),
            carbon_dash.ToggleSmall(
                id='gallery-togglesmall',
                
                
                
                
            ),
            html.Hr()
        ], style={'padding': '20px'}),

        html.Section([
            html.H3("Toggletip"),
            carbon_dash.Toggletip(
                id='gallery-toggletip',
                
                
                
                
            ),
            html.Hr()
        ], style={'padding': '20px'}),

        html.Section([
            html.H3("TreeView"),
            carbon_dash.TreeView(
                id='gallery-treeview',
                
                
                
                
            ),
            html.Hr()
        ], style={'padding': '20px'}),

        html.Section([
            html.H3("UIShell"),
            carbon_dash.UIShell(
                id='gallery-uishell',
                
                
                
                
            ),
            html.Hr()
        ], style={'padding': '20px'}),

        html.Section([
            html.H3("UnorderedList"),
            carbon_dash.UnorderedList(
                id='gallery-unorderedlist',
                
                
                
                
            ),
            html.Hr()
        ], style={'padding': '20px'}),

    ])
])

if __name__ == "__main__":
    import sys
    port = 8052
    if len(sys.argv) > 1 and sys.argv[1] == "--port":
        port = int(sys.argv[2])
    app.run(debug=True, port=port)
