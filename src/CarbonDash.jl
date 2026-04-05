
module CarbonDash
using Dash

const resources_path = realpath(joinpath( @__DIR__, "..", "deps"))
const version = "0.0.1"

include("jl/ailabel.jl")
include("jl/ailabelactions.jl")
include("jl/ailabelcontent.jl")
include("jl/aiskeletonicon.jl")
include("jl/aiskeletonplaceholder.jl")
include("jl/aiskeletontext.jl")
include("jl/accordion.jl")
include("jl/accordionitem.jl")
include("jl/accordionskeleton.jl")
include("jl/actionablenotification.jl")
include("jl/aspectratio.jl")
include("jl/breadcrumb.jl")
include("jl/breadcrumbitem.jl")
include("jl/breadcrumbskeleton.jl")
include("jl/button.jl")
include("jl/buttonset.jl")
include("jl/buttonskeleton.jl")
include("jl/callout.jl")
include("jl/chatbutton.jl")
include("jl/chatbuttonskeleton.jl")
include("jl/checkbox.jl")
include("jl/checkboxgroup.jl")
include("jl/checkboxskeleton.jl")
include("jl/classprefix.jl")
include("jl/clickabletile.jl")
include("jl/codesnippet.jl")
include("jl/codesnippetskeleton.jl")
include("jl/column.jl")
include("jl/columnhang.jl")
include("jl/combobox.jl")
include("jl/combobutton.jl")
include("jl/composedmodal.jl")
include("jl/composedmodalpresence.jl")
include("jl/containedlist.jl")
include("jl/containedlistitem.jl")
include("jl/content.jl")
include("jl/contentswitcher.jl")
include("jl/controlledpasswordinput.jl")
include("jl/copy.jl")
include("jl/copybutton.jl")
include("jl/dangerbutton.jl")
include("jl/datatable.jl")
include("jl/datatableskeleton.jl")
include("jl/datepicker.jl")
include("jl/datepickerinput.jl")
include("jl/datepickerskeleton.jl")
include("jl/definitiontooltip.jl")
include("jl/dismissibletag.jl")
include("jl/dropdown.jl")
include("jl/dropdownskeleton.jl")
include("jl/errorboundary.jl")
include("jl/errorboundarycontext.jl")
include("jl/expandablesearch.jl")
include("jl/expandabletile.jl")
include("jl/featureflags.jl")
include("jl/fileuploader.jl")
include("jl/fileuploaderbutton.jl")
include("jl/fileuploaderdropcontainer.jl")
include("jl/fileuploaderitem.jl")
include("jl/fileuploaderskeleton.jl")
include("jl/filename.jl")
include("jl/filterablemultiselect.jl")
include("jl/flexgrid.jl")
include("jl/fluidcombobox.jl")
include("jl/fluidcomboboxskeleton.jl")
include("jl/fluiddatepicker.jl")
include("jl/fluiddatepickerinput.jl")
include("jl/fluiddatepickerskeleton.jl")
include("jl/fluiddropdown.jl")
include("jl/fluiddropdownskeleton.jl")
include("jl/fluidform.jl")
include("jl/fluidmultiselect.jl")
include("jl/fluidmultiselectskeleton.jl")
include("jl/fluidnumberinput.jl")
include("jl/fluidnumberinputskeleton.jl")
include("jl/fluidpasswordinput.jl")
include("jl/fluidsearch.jl")
include("jl/fluidsearchskeleton.jl")
include("jl/fluidselect.jl")
include("jl/fluidselectskeleton.jl")
include("jl/fluidtextarea.jl")
include("jl/fluidtextareaskeleton.jl")
include("jl/fluidtextinput.jl")
include("jl/fluidtextinputskeleton.jl")
include("jl/fluidtimepicker.jl")
include("jl/fluidtimepickerselect.jl")
include("jl/fluidtimepickerskeleton.jl")
include("jl/form.jl")
include("jl/formcontext.jl")
include("jl/formgroup.jl")
include("jl/formitem.jl")
include("jl/formlabel.jl")
include("jl/globaltheme.jl")
include("jl/grid.jl")
include("jl/gridsettings.jl")
include("jl/hstack.jl")
include("jl/header.jl")
include("jl/headercontainer.jl")
include("jl/headerglobalaction.jl")
include("jl/headerglobalbar.jl")
include("jl/headermenu.jl")
include("jl/headermenubutton.jl")
include("jl/headermenuitem.jl")
include("jl/headername.jl")
include("jl/headernavigation.jl")
include("jl/headerpanel.jl")
include("jl/headersidenavitems.jl")
include("jl/heading.jl")
include("jl/iconbutton.jl")
include("jl/iconindicator.jl")
include("jl/iconskeleton.jl")
include("jl/iconswitch.jl")
include("jl/icontab.jl")
include("jl/idprefix.jl")
include("jl/inlineloading.jl")
include("jl/inlinenotification.jl")
include("jl/layer.jl")
include("jl/link.jl")
include("jl/listitem.jl")
include("jl/loading.jl")
include("jl/menu.jl")
include("jl/menubutton.jl")
include("jl/menuitem.jl")
include("jl/menuitemdivider.jl")
include("jl/menuitemgroup.jl")
include("jl/menuitemradiogroup.jl")
include("jl/menuitemselectable.jl")
include("jl/modal.jl")
include("jl/modalbody.jl")
include("jl/modalfooter.jl")
include("jl/modalheader.jl")
include("jl/modalpresence.jl")
include("jl/modalwrapper.jl")
include("jl/multiselect.jl")
include("jl/notificationactionbutton.jl")
include("jl/notificationbutton.jl")
include("jl/numberinput.jl")
include("jl/numberinputskeleton.jl")
include("jl/operationaltag.jl")
include("jl/orderedlist.jl")
include("jl/overflowmenu.jl")
include("jl/overflowmenuitem.jl")
include("jl/pagination.jl")
include("jl/paginationnav.jl")
include("jl/paginationskeleton.jl")
include("jl/passwordinput.jl")
include("jl/popover.jl")
include("jl/popovercontent.jl")
include("jl/prefixcontext.jl")
include("jl/primarybutton.jl")
include("jl/progressbar.jl")
include("jl/progressindicator.jl")
include("jl/progressindicatorskeleton.jl")
include("jl/progressstep.jl")
include("jl/radiobutton.jl")
include("jl/radiobuttongroup.jl")
include("jl/radiobuttonskeleton.jl")
include("jl/radiotile.jl")
include("jl/row.jl")
include("jl/search.jl")
include("jl/searchskeleton.jl")
include("jl/secondarybutton.jl")
include("jl/section.jl")
include("jl/select.jl")
include("jl/selectitem.jl")
include("jl/selectitemgroup.jl")
include("jl/selectskeleton.jl")
include("jl/selectabletag.jl")
include("jl/selectabletile.jl")
include("jl/shapeindicator.jl")
include("jl/sidenav.jl")
include("jl/sidenavdetails.jl")
include("jl/sidenavdivider.jl")
include("jl/sidenavfooter.jl")
include("jl/sidenavheader.jl")
include("jl/sidenavicon.jl")
include("jl/sidenavitem.jl")
include("jl/sidenavitems.jl")
include("jl/sidenavlink.jl")
include("jl/sidenavlinktext.jl")
include("jl/sidenavmenu.jl")
include("jl/sidenavmenuitem.jl")
include("jl/sidenavswitcher.jl")
include("jl/skeletonicon.jl")
include("jl/skeletonplaceholder.jl")
include("jl/skeletontext.jl")
include("jl/skiptocontent.jl")
include("jl/slider.jl")
include("jl/sliderskeleton.jl")
include("jl/slug.jl")
include("jl/slugactions.jl")
include("jl/slugcontent.jl")
include("jl/stack.jl")
include("jl/staticnotification.jl")
include("jl/structuredlistbody.jl")
include("jl/structuredlistcell.jl")
include("jl/structuredlisthead.jl")
include("jl/structuredlistinput.jl")
include("jl/structuredlistrow.jl")
include("jl/structuredlistskeleton.jl")
include("jl/structuredlistwrapper.jl")
include("jl/switch.jl")
include("jl/switcher.jl")
include("jl/switcherdivider.jl")
include("jl/switcheritem.jl")
include("jl/tab.jl")
include("jl/tabcontent.jl")
include("jl/tablist.jl")
include("jl/tablistvertical.jl")
include("jl/tabpanel.jl")
include("jl/tabpanels.jl")
include("jl/table.jl")
include("jl/tableactionlist.jl")
include("jl/tablebatchaction.jl")
include("jl/tablebatchactions.jl")
include("jl/tablebody.jl")
include("jl/tablecell.jl")
include("jl/tablecontainer.jl")
include("jl/tabledecoratorrow.jl")
include("jl/tableexpandheader.jl")
include("jl/tableexpandrow.jl")
include("jl/tableexpandedrow.jl")
include("jl/tablehead.jl")
include("jl/tableheader.jl")
include("jl/tablerow.jl")
include("jl/tableselectall.jl")
include("jl/tableselectrow.jl")
include("jl/tableslugrow.jl")
include("jl/tabletoolbar.jl")
include("jl/tabletoolbaraction.jl")
include("jl/tabletoolbarcontent.jl")
include("jl/tabletoolbarmenu.jl")
include("jl/tabletoolbarsearch.jl")
include("jl/tabs.jl")
include("jl/tabsskeleton.jl")
include("jl/tabsvertical.jl")
include("jl/tag.jl")
include("jl/tagskeleton.jl")
include("jl/textarea.jl")
include("jl/textareaskeleton.jl")
include("jl/textinput.jl")
include("jl/textinputskeleton.jl")
include("jl/theme.jl")
include("jl/themecontext.jl")
include("jl/tile.jl")
include("jl/tileabovethefoldcontent.jl")
include("jl/tilebelowthefoldcontent.jl")
include("jl/tilegroup.jl")
include("jl/timepicker.jl")
include("jl/timepickerselect.jl")
include("jl/toastnotification.jl")
include("jl/toggle.jl")
include("jl/toggleskeleton.jl")
include("jl/togglesmallskeleton.jl")
include("jl/toggletip.jl")
include("jl/toggletipactions.jl")
include("jl/toggletipbutton.jl")
include("jl/toggletipcontent.jl")
include("jl/toggletiplabel.jl")
include("jl/tooltip.jl")
include("jl/treenode.jl")
include("jl/treeview.jl")
include("jl/unorderedlist.jl")
include("jl/vstack.jl")

function __init__()
    DashBase.register_package(
        DashBase.ResourcePkg(
            "carbon_dash",
            resources_path,
            version = version,
            [
                DashBase.Resource(
    relative_package_path = "async-HeaderName.js",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-HeaderName.js",
    dynamic = nothing,
    async = :true,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-Slider.js",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-Slider.js",
    dynamic = nothing,
    async = :true,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-TabsVertical.js",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-TabsVertical.js",
    dynamic = nothing,
    async = :true,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-ErrorBoundaryContext.js",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-ErrorBoundaryContext.js",
    dynamic = nothing,
    async = :true,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-ButtonSkeleton.js",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-ButtonSkeleton.js",
    dynamic = nothing,
    async = :true,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-BadgeIndicator.js",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-BadgeIndicator.js",
    dynamic = nothing,
    async = :true,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-HeaderSideNavItems.js",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-HeaderSideNavItems.js",
    dynamic = nothing,
    async = :true,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-ProgressIndicatorSkeleton.js",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-ProgressIndicatorSkeleton.js",
    dynamic = nothing,
    async = :true,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-ToggletipButton.js",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-ToggletipButton.js",
    dynamic = nothing,
    async = :true,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-NumberInputSkeleton.js",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-NumberInputSkeleton.js",
    dynamic = nothing,
    async = :true,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-Copy.js",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-Copy.js",
    dynamic = nothing,
    async = :true,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-ModalWrapper.js",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-ModalWrapper.js",
    dynamic = nothing,
    async = :true,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-CodeSnippetSkeleton.js",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-CodeSnippetSkeleton.js",
    dynamic = nothing,
    async = :true,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-MenuItemDivider.js",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-MenuItemDivider.js",
    dynamic = nothing,
    async = :true,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-BreadcrumbItem.js",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-BreadcrumbItem.js",
    dynamic = nothing,
    async = :true,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-AILabelContent.js",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-AILabelContent.js",
    dynamic = nothing,
    async = :true,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-ErrorBoundary.js",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-ErrorBoundary.js",
    dynamic = nothing,
    async = :true,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-InlineCheckbox.js",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-InlineCheckbox.js",
    dynamic = nothing,
    async = :true,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-LayoutDirection.js",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-LayoutDirection.js",
    dynamic = nothing,
    async = :true,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-StructuredListSkeleton.js",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-StructuredListSkeleton.js",
    dynamic = nothing,
    async = :true,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-ModalFooter.js",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-ModalFooter.js",
    dynamic = nothing,
    async = :true,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-Plex.js",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-Plex.js",
    dynamic = nothing,
    async = :true,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-ComposedModal.js",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-ComposedModal.js",
    dynamic = nothing,
    async = :true,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-RadioButtonSkeleton.js",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-RadioButtonSkeleton.js",
    dynamic = nothing,
    async = :true,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-ClassPrefix.js",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-ClassPrefix.js",
    dynamic = nothing,
    async = :true,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-ContextMenu.js",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-ContextMenu.js",
    dynamic = nothing,
    async = :true,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-TextInput.js",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-TextInput.js",
    dynamic = nothing,
    async = :true,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-ExpandableSearch.js",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-ExpandableSearch.js",
    dynamic = nothing,
    async = :true,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-Filename.js",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-Filename.js",
    dynamic = nothing,
    async = :true,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-TableToolbarContent.js",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-TableToolbarContent.js",
    dynamic = nothing,
    async = :true,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-FileUploaderDropContainer.js",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-FileUploaderDropContainer.js",
    dynamic = nothing,
    async = :true,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-SecondaryButton.js",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-SecondaryButton.js",
    dynamic = nothing,
    async = :true,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-TabContent.js",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-TabContent.js",
    dynamic = nothing,
    async = :true,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-StructuredListWrapper.js",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-StructuredListWrapper.js",
    dynamic = nothing,
    async = :true,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-FluidTextInputSkeleton.js",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-FluidTextInputSkeleton.js",
    dynamic = nothing,
    async = :true,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-FileUploader.js",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-FileUploader.js",
    dynamic = nothing,
    async = :true,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-FluidDatePicker.js",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-FluidDatePicker.js",
    dynamic = nothing,
    async = :true,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-Checkbox.js",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-Checkbox.js",
    dynamic = nothing,
    async = :true,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-SlugActions.js",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-SlugActions.js",
    dynamic = nothing,
    async = :true,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-Button.js",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-Button.js",
    dynamic = nothing,
    async = :true,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-MenuItemGroup.js",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-MenuItemGroup.js",
    dynamic = nothing,
    async = :true,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-SliderSkeleton.js",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-SliderSkeleton.js",
    dynamic = nothing,
    async = :true,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-SkeletonPlaceholder.js",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-SkeletonPlaceholder.js",
    dynamic = nothing,
    async = :true,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-NotificationButton.js",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-NotificationButton.js",
    dynamic = nothing,
    async = :true,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-TableHead.js",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-TableHead.js",
    dynamic = nothing,
    async = :true,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-ContainedListItem.js",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-ContainedListItem.js",
    dynamic = nothing,
    async = :true,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-HeaderMenuItem.js",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-HeaderMenuItem.js",
    dynamic = nothing,
    async = :true,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-DatePickerSkeleton.js",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-DatePickerSkeleton.js",
    dynamic = nothing,
    async = :true,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-TableToolbarMenu.js",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-TableToolbarMenu.js",
    dynamic = nothing,
    async = :true,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-ButtonSet.js",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-ButtonSet.js",
    dynamic = nothing,
    async = :true,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-TableRow.js",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-TableRow.js",
    dynamic = nothing,
    async = :true,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-PasswordInput.js",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-PasswordInput.js",
    dynamic = nothing,
    async = :true,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-Icons.js",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-Icons.js",
    dynamic = nothing,
    async = :true,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-Content.js",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-Content.js",
    dynamic = nothing,
    async = :true,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-AccordionSkeleton.js",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-AccordionSkeleton.js",
    dynamic = nothing,
    async = :true,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-TableActionList.js",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-TableActionList.js",
    dynamic = nothing,
    async = :true,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-CodeSnippet.js",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-CodeSnippet.js",
    dynamic = nothing,
    async = :true,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-FormLabel.js",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-FormLabel.js",
    dynamic = nothing,
    async = :true,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-StructuredListHead.js",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-StructuredListHead.js",
    dynamic = nothing,
    async = :true,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-IconSwitch.js",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-IconSwitch.js",
    dynamic = nothing,
    async = :true,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-FluidSearch.js",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-FluidSearch.js",
    dynamic = nothing,
    async = :true,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-Notification.js",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-Notification.js",
    dynamic = nothing,
    async = :true,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-FluidTimePickerSelect.js",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-FluidTimePickerSelect.js",
    dynamic = nothing,
    async = :true,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-FluidTimePicker.js",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-FluidTimePicker.js",
    dynamic = nothing,
    async = :true,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-Dropdown.js",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-Dropdown.js",
    dynamic = nothing,
    async = :true,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-FormGroup.js",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-FormGroup.js",
    dynamic = nothing,
    async = :true,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-ToggleSmallSkeleton.js",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-ToggleSmallSkeleton.js",
    dynamic = nothing,
    async = :true,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-StructuredListRow.js",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-StructuredListRow.js",
    dynamic = nothing,
    async = :true,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-IconIndicator.js",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-IconIndicator.js",
    dynamic = nothing,
    async = :true,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-Search.js",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-Search.js",
    dynamic = nothing,
    async = :true,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-OrderedList.js",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-OrderedList.js",
    dynamic = nothing,
    async = :true,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-TableExpandedRow.js",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-TableExpandedRow.js",
    dynamic = nothing,
    async = :true,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-ToggletipContent.js",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-ToggletipContent.js",
    dynamic = nothing,
    async = :true,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-SideNavFooter.js",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-SideNavFooter.js",
    dynamic = nothing,
    async = :true,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-TableHeader.js",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-TableHeader.js",
    dynamic = nothing,
    async = :true,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-IconTab.js",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-IconTab.js",
    dynamic = nothing,
    async = :true,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-TableToolbarAction.js",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-TableToolbarAction.js",
    dynamic = nothing,
    async = :true,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-AccordionItem.js",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-AccordionItem.js",
    dynamic = nothing,
    async = :true,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-OverflowMenuV2.js",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-OverflowMenuV2.js",
    dynamic = nothing,
    async = :true,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-MenuButton.js",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-MenuButton.js",
    dynamic = nothing,
    async = :true,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-FluidNumberInputSkeleton.js",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-FluidNumberInputSkeleton.js",
    dynamic = nothing,
    async = :true,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-Pagination.js",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-Pagination.js",
    dynamic = nothing,
    async = :true,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-Heading.js",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-Heading.js",
    dynamic = nothing,
    async = :true,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-MenuItemRadioGroup.js",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-MenuItemRadioGroup.js",
    dynamic = nothing,
    async = :true,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-Select.js",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-Select.js",
    dynamic = nothing,
    async = :true,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-SideNavItems.js",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-SideNavItems.js",
    dynamic = nothing,
    async = :true,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-SideNavLinkText.js",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-SideNavLinkText.js",
    dynamic = nothing,
    async = :true,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-StaticNotification.js",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-StaticNotification.js",
    dynamic = nothing,
    async = :true,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-AISkeletonText.js",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-AISkeletonText.js",
    dynamic = nothing,
    async = :true,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-FormItem.js",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-FormItem.js",
    dynamic = nothing,
    async = :true,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-ButtonKinds.js",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-ButtonKinds.js",
    dynamic = nothing,
    async = :true,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-NotificationActionButton.js",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-NotificationActionButton.js",
    dynamic = nothing,
    async = :true,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-ModalBody.js",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-ModalBody.js",
    dynamic = nothing,
    async = :true,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-ComposedModalPresence.js",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-ComposedModalPresence.js",
    dynamic = nothing,
    async = :true,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-NumberInput.js",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-NumberInput.js",
    dynamic = nothing,
    async = :true,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-SelectItem.js",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-SelectItem.js",
    dynamic = nothing,
    async = :true,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-ToggleSkeleton.js",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-ToggleSkeleton.js",
    dynamic = nothing,
    async = :true,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-ProgressIndicator.js",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-ProgressIndicator.js",
    dynamic = nothing,
    async = :true,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-FluidForm.js",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-FluidForm.js",
    dynamic = nothing,
    async = :true,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-PrimaryButton.js",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-PrimaryButton.js",
    dynamic = nothing,
    async = :true,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-PrefixContext.js",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-PrefixContext.js",
    dynamic = nothing,
    async = :true,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-SkeletonText.js",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-SkeletonText.js",
    dynamic = nothing,
    async = :true,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-HeaderGlobalAction.js",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-HeaderGlobalAction.js",
    dynamic = nothing,
    async = :true,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-TabsSkeleton.js",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-TabsSkeleton.js",
    dynamic = nothing,
    async = :true,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-ChatButtonSkeleton.js",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-ChatButtonSkeleton.js",
    dynamic = nothing,
    async = :true,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-Tag.js",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-Tag.js",
    dynamic = nothing,
    async = :true,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-ChatButton.js",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-ChatButton.js",
    dynamic = nothing,
    async = :true,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-AILabel.js",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-AILabel.js",
    dynamic = nothing,
    async = :true,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-ListBox.js",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-ListBox.js",
    dynamic = nothing,
    async = :true,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-InlineNotification.js",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-InlineNotification.js",
    dynamic = nothing,
    async = :true,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-ProgressStep.js",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-ProgressStep.js",
    dynamic = nothing,
    async = :true,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-DatePicker.js",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-DatePicker.js",
    dynamic = nothing,
    async = :true,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-SideNavLink.js",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-SideNavLink.js",
    dynamic = nothing,
    async = :true,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-ToggletipLabel.js",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-ToggletipLabel.js",
    dynamic = nothing,
    async = :true,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-FluidSelectSkeleton.js",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-FluidSelectSkeleton.js",
    dynamic = nothing,
    async = :true,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-SideNavIcon.js",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-SideNavIcon.js",
    dynamic = nothing,
    async = :true,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-UnorderedList.js",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-UnorderedList.js",
    dynamic = nothing,
    async = :true,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-TableBatchActions.js",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-TableBatchActions.js",
    dynamic = nothing,
    async = :true,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-Theme.js",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-Theme.js",
    dynamic = nothing,
    async = :true,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-DataTable.js",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-DataTable.js",
    dynamic = nothing,
    async = :true,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-RadioButtonGroup.js",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-RadioButtonGroup.js",
    dynamic = nothing,
    async = :true,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-FluidSelect.js",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-FluidSelect.js",
    dynamic = nothing,
    async = :true,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-Tabs.js",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-Tabs.js",
    dynamic = nothing,
    async = :true,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-TableSelectRow.js",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-TableSelectRow.js",
    dynamic = nothing,
    async = :true,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-HeaderMenu.js",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-HeaderMenu.js",
    dynamic = nothing,
    async = :true,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-Callout.js",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-Callout.js",
    dynamic = nothing,
    async = :true,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-ComboButton.js",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-ComboButton.js",
    dynamic = nothing,
    async = :true,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-Icon.js",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-Icon.js",
    dynamic = nothing,
    async = :true,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-Link.js",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-Link.js",
    dynamic = nothing,
    async = :true,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-Tile.js",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-Tile.js",
    dynamic = nothing,
    async = :true,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-FluidDropdown.js",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-FluidDropdown.js",
    dynamic = nothing,
    async = :true,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-InlineLoading.js",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-InlineLoading.js",
    dynamic = nothing,
    async = :true,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-TableToolbar.js",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-TableToolbar.js",
    dynamic = nothing,
    async = :true,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-AspectRatio.js",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-AspectRatio.js",
    dynamic = nothing,
    async = :true,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-IconSkeleton.js",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-IconSkeleton.js",
    dynamic = nothing,
    async = :true,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-DismissibleTag.js",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-DismissibleTag.js",
    dynamic = nothing,
    async = :true,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-BreadcrumbSkeleton.js",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-BreadcrumbSkeleton.js",
    dynamic = nothing,
    async = :true,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-ClickableTile.js",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-ClickableTile.js",
    dynamic = nothing,
    async = :true,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-SelectableTile.js",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-SelectableTile.js",
    dynamic = nothing,
    async = :true,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-GridSettings.js",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-GridSettings.js",
    dynamic = nothing,
    async = :true,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-MenuItemSelectable.js",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-MenuItemSelectable.js",
    dynamic = nothing,
    async = :true,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-Grid.js",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-Grid.js",
    dynamic = nothing,
    async = :true,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-ButtonSizes.js",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-ButtonSizes.js",
    dynamic = nothing,
    async = :true,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-Tab.js",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-Tab.js",
    dynamic = nothing,
    async = :true,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-MenuItem.js",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-MenuItem.js",
    dynamic = nothing,
    async = :true,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-ProgressBar.js",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-ProgressBar.js",
    dynamic = nothing,
    async = :true,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-SideNavDetails.js",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-SideNavDetails.js",
    dynamic = nothing,
    async = :true,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-FluidMultiSelect.js",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-FluidMultiSelect.js",
    dynamic = nothing,
    async = :true,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-SelectSkeleton.js",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-SelectSkeleton.js",
    dynamic = nothing,
    async = :true,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-Row.js",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-Row.js",
    dynamic = nothing,
    async = :true,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-TimePickerSelect.js",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-TimePickerSelect.js",
    dynamic = nothing,
    async = :true,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-TimePicker.js",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-TimePicker.js",
    dynamic = nothing,
    async = :true,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-FluidComboBoxSkeleton.js",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-FluidComboBoxSkeleton.js",
    dynamic = nothing,
    async = :true,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-SideNavMenuItem.js",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-SideNavMenuItem.js",
    dynamic = nothing,
    async = :true,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-Popover.js",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-Popover.js",
    dynamic = nothing,
    async = :true,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-Column.js",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-Column.js",
    dynamic = nothing,
    async = :true,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-OperationalTag.js",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-OperationalTag.js",
    dynamic = nothing,
    async = :true,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-ThemeContext.js",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-ThemeContext.js",
    dynamic = nothing,
    async = :true,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-FluidNumberInput.js",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-FluidNumberInput.js",
    dynamic = nothing,
    async = :true,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-PageHeader.js",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-PageHeader.js",
    dynamic = nothing,
    async = :true,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-CarbonDash.js",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-CarbonDash.js",
    dynamic = nothing,
    async = :true,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-ModalHeader.js",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-ModalHeader.js",
    dynamic = nothing,
    async = :true,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-Slug.js",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-Slug.js",
    dynamic = nothing,
    async = :true,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-FilterableMultiSelect.js",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-FilterableMultiSelect.js",
    dynamic = nothing,
    async = :true,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-Toggle.js",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-Toggle.js",
    dynamic = nothing,
    async = :true,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-TableSlugRow.js",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-TableSlugRow.js",
    dynamic = nothing,
    async = :true,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-AISkeletonPlaceholder.js",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-AISkeletonPlaceholder.js",
    dynamic = nothing,
    async = :true,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-ActionableNotification.js",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-ActionableNotification.js",
    dynamic = nothing,
    async = :true,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-UIShell.js",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-UIShell.js",
    dynamic = nothing,
    async = :true,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-OverflowMenuItem.js",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-OverflowMenuItem.js",
    dynamic = nothing,
    async = :true,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-FluidDropdownSkeleton.js",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-FluidDropdownSkeleton.js",
    dynamic = nothing,
    async = :true,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-Switcher.js",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-Switcher.js",
    dynamic = nothing,
    async = :true,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-RadioTile.js",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-RadioTile.js",
    dynamic = nothing,
    async = :true,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-FluidDatePickerInput.js",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-FluidDatePickerInput.js",
    dynamic = nothing,
    async = :true,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-ModalPresence.js",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-ModalPresence.js",
    dynamic = nothing,
    async = :true,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-HeaderNavigation.js",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-HeaderNavigation.js",
    dynamic = nothing,
    async = :true,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-SkipToContent.js",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-SkipToContent.js",
    dynamic = nothing,
    async = :true,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-ToastNotification.js",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-ToastNotification.js",
    dynamic = nothing,
    async = :true,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-FluidMultiSelectSkeleton.js",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-FluidMultiSelectSkeleton.js",
    dynamic = nothing,
    async = :true,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-HeaderMenuButton.js",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-HeaderMenuButton.js",
    dynamic = nothing,
    async = :true,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-TabListVertical.js",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-TabListVertical.js",
    dynamic = nothing,
    async = :true,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-TreeNode.js",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-TreeNode.js",
    dynamic = nothing,
    async = :true,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-TableDecoratorRow.js",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-TableDecoratorRow.js",
    dynamic = nothing,
    async = :true,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-SideNavSwitcher.js",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-SideNavSwitcher.js",
    dynamic = nothing,
    async = :true,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-RadioButton.js",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-RadioButton.js",
    dynamic = nothing,
    async = :true,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-FluidTextArea.js",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-FluidTextArea.js",
    dynamic = nothing,
    async = :true,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-SideNavHeader.js",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-SideNavHeader.js",
    dynamic = nothing,
    async = :true,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-HeaderGlobalBar.js",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-HeaderGlobalBar.js",
    dynamic = nothing,
    async = :true,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-TileAboveTheFoldContent.js",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-TileAboveTheFoldContent.js",
    dynamic = nothing,
    async = :true,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-Portal.js",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-Portal.js",
    dynamic = nothing,
    async = :true,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-TableBody.js",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-TableBody.js",
    dynamic = nothing,
    async = :true,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-PaginationNav.js",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-PaginationNav.js",
    dynamic = nothing,
    async = :true,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-SideNavItem.js",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-SideNavItem.js",
    dynamic = nothing,
    async = :true,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-Disclosure.js",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-Disclosure.js",
    dynamic = nothing,
    async = :true,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-Table.js",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-Table.js",
    dynamic = nothing,
    async = :true,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-TileBelowTheFoldContent.js",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-TileBelowTheFoldContent.js",
    dynamic = nothing,
    async = :true,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-VStack.js",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-VStack.js",
    dynamic = nothing,
    async = :true,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-CheckboxGroup.js",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-CheckboxGroup.js",
    dynamic = nothing,
    async = :true,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-StructuredListBody.js",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-StructuredListBody.js",
    dynamic = nothing,
    async = :true,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-FluidComboBox.js",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-FluidComboBox.js",
    dynamic = nothing,
    async = :true,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-Loading.js",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-Loading.js",
    dynamic = nothing,
    async = :true,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-DataTableSkeleton.js",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-DataTableSkeleton.js",
    dynamic = nothing,
    async = :true,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-StructuredListInput.js",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-StructuredListInput.js",
    dynamic = nothing,
    async = :true,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-ButtonTooltipAlignments.js",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-ButtonTooltipAlignments.js",
    dynamic = nothing,
    async = :true,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-IdPrefix.js",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-IdPrefix.js",
    dynamic = nothing,
    async = :true,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-SelectableTag.js",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-SelectableTag.js",
    dynamic = nothing,
    async = :true,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-PopoverContent.js",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-PopoverContent.js",
    dynamic = nothing,
    async = :true,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-Dialog.js",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-Dialog.js",
    dynamic = nothing,
    async = :true,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-ContainedList.js",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-ContainedList.js",
    dynamic = nothing,
    async = :true,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-MultiSelect.js",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-MultiSelect.js",
    dynamic = nothing,
    async = :true,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-FluidTextAreaSkeleton.js",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-FluidTextAreaSkeleton.js",
    dynamic = nothing,
    async = :true,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-SideNavDivider.js",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-SideNavDivider.js",
    dynamic = nothing,
    async = :true,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-TableExpandHeader.js",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-TableExpandHeader.js",
    dynamic = nothing,
    async = :true,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-PaginationSkeleton.js",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-PaginationSkeleton.js",
    dynamic = nothing,
    async = :true,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-SwitcherItem.js",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-SwitcherItem.js",
    dynamic = nothing,
    async = :true,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-Header.js",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-Header.js",
    dynamic = nothing,
    async = :true,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-AISkeleton.js",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-AISkeleton.js",
    dynamic = nothing,
    async = :true,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-DangerButton.js",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-DangerButton.js",
    dynamic = nothing,
    async = :true,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-TileGroup.js",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-TileGroup.js",
    dynamic = nothing,
    async = :true,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-TabList.js",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-TabList.js",
    dynamic = nothing,
    async = :true,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-SideNav.js",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-SideNav.js",
    dynamic = nothing,
    async = :true,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-ToggleSmall.js",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-ToggleSmall.js",
    dynamic = nothing,
    async = :true,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-TableBatchAction.js",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-TableBatchAction.js",
    dynamic = nothing,
    async = :true,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-ShapeIndicator.js",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-ShapeIndicator.js",
    dynamic = nothing,
    async = :true,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-DefinitionTooltip.js",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-DefinitionTooltip.js",
    dynamic = nothing,
    async = :true,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-TreeView.js",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-TreeView.js",
    dynamic = nothing,
    async = :true,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-GlobalTheme.js",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-GlobalTheme.js",
    dynamic = nothing,
    async = :true,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-Tooltip.js",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-Tooltip.js",
    dynamic = nothing,
    async = :true,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-ControlledPasswordInput.js",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-ControlledPasswordInput.js",
    dynamic = nothing,
    async = :true,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-OverflowMenu.js",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-OverflowMenu.js",
    dynamic = nothing,
    async = :true,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-TableCell.js",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-TableCell.js",
    dynamic = nothing,
    async = :true,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-IconButton.js",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-IconButton.js",
    dynamic = nothing,
    async = :true,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-Section.js",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-Section.js",
    dynamic = nothing,
    async = :true,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-FluidDatePickerSkeleton.js",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-FluidDatePickerSkeleton.js",
    dynamic = nothing,
    async = :true,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-Layout.js",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-Layout.js",
    dynamic = nothing,
    async = :true,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-TagSkeleton.js",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-TagSkeleton.js",
    dynamic = nothing,
    async = :true,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-ToggletipActions.js",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-ToggletipActions.js",
    dynamic = nothing,
    async = :true,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-FileUploaderItem.js",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-FileUploaderItem.js",
    dynamic = nothing,
    async = :true,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-Stack.js",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-Stack.js",
    dynamic = nothing,
    async = :true,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-Text.js",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-Text.js",
    dynamic = nothing,
    async = :true,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-StructuredListCell.js",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-StructuredListCell.js",
    dynamic = nothing,
    async = :true,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-ContentSwitcher.js",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-ContentSwitcher.js",
    dynamic = nothing,
    async = :true,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-TextInputSkeleton.js",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-TextInputSkeleton.js",
    dynamic = nothing,
    async = :true,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-FileUploaderButton.js",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-FileUploaderButton.js",
    dynamic = nothing,
    async = :true,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-DatePickerInput.js",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-DatePickerInput.js",
    dynamic = nothing,
    async = :true,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-Toggletip.js",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-Toggletip.js",
    dynamic = nothing,
    async = :true,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-FluidTimePickerSkeleton.js",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-FluidTimePickerSkeleton.js",
    dynamic = nothing,
    async = :true,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-CheckboxSkeleton.js",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-CheckboxSkeleton.js",
    dynamic = nothing,
    async = :true,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-IconButtonKinds.js",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-IconButtonKinds.js",
    dynamic = nothing,
    async = :true,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-ButtonTooltipPositions.js",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-ButtonTooltipPositions.js",
    dynamic = nothing,
    async = :true,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-HeaderPanel.js",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-HeaderPanel.js",
    dynamic = nothing,
    async = :true,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-FileUploaderSkeleton.js",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-FileUploaderSkeleton.js",
    dynamic = nothing,
    async = :true,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-Modal.js",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-Modal.js",
    dynamic = nothing,
    async = :true,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-FluidSearchSkeleton.js",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-FluidSearchSkeleton.js",
    dynamic = nothing,
    async = :true,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-HStack.js",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-HStack.js",
    dynamic = nothing,
    async = :true,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-FluidTextInput.js",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-FluidTextInput.js",
    dynamic = nothing,
    async = :true,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-DropdownSkeleton.js",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-DropdownSkeleton.js",
    dynamic = nothing,
    async = :true,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-Accordion.js",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-Accordion.js",
    dynamic = nothing,
    async = :true,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-SideNavMenu.js",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-SideNavMenu.js",
    dynamic = nothing,
    async = :true,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-TableExpandRow.js",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-TableExpandRow.js",
    dynamic = nothing,
    async = :true,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-Layer.js",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-Layer.js",
    dynamic = nothing,
    async = :true,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-SkeletonIcon.js",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-SkeletonIcon.js",
    dynamic = nothing,
    async = :true,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-TextAreaSkeleton.js",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-TextAreaSkeleton.js",
    dynamic = nothing,
    async = :true,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-SwitcherDivider.js",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-SwitcherDivider.js",
    dynamic = nothing,
    async = :true,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-FlexGrid.js",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-FlexGrid.js",
    dynamic = nothing,
    async = :true,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-Breadcrumb.js",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-Breadcrumb.js",
    dynamic = nothing,
    async = :true,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-AISkeletonIcon.js",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-AISkeletonIcon.js",
    dynamic = nothing,
    async = :true,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-StructuredList.js",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-StructuredList.js",
    dynamic = nothing,
    async = :true,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-FluidPasswordInput.js",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-FluidPasswordInput.js",
    dynamic = nothing,
    async = :true,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-HeaderContainer.js",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-HeaderContainer.js",
    dynamic = nothing,
    async = :true,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-SlugContent.js",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-SlugContent.js",
    dynamic = nothing,
    async = :true,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-TabPanels.js",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-TabPanels.js",
    dynamic = nothing,
    async = :true,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-Menu.js",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-Menu.js",
    dynamic = nothing,
    async = :true,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-Switch.js",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-Switch.js",
    dynamic = nothing,
    async = :true,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-CopyButton.js",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-CopyButton.js",
    dynamic = nothing,
    async = :true,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-Form.js",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-Form.js",
    dynamic = nothing,
    async = :true,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-ColumnHang.js",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-ColumnHang.js",
    dynamic = nothing,
    async = :true,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-FeatureFlags.js",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-FeatureFlags.js",
    dynamic = nothing,
    async = :true,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-FormContext.js",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-FormContext.js",
    dynamic = nothing,
    async = :true,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-TextArea.js",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-TextArea.js",
    dynamic = nothing,
    async = :true,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-TableContainer.js",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-TableContainer.js",
    dynamic = nothing,
    async = :true,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-ComboBox.js",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-ComboBox.js",
    dynamic = nothing,
    async = :true,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-ListItem.js",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-ListItem.js",
    dynamic = nothing,
    async = :true,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-TableToolbarSearch.js",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-TableToolbarSearch.js",
    dynamic = nothing,
    async = :true,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-SearchSkeleton.js",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-SearchSkeleton.js",
    dynamic = nothing,
    async = :true,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-SelectItemGroup.js",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-SelectItemGroup.js",
    dynamic = nothing,
    async = :true,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-TableSelectAll.js",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-TableSelectAll.js",
    dynamic = nothing,
    async = :true,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-HideAtBreakpoint.js",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-HideAtBreakpoint.js",
    dynamic = nothing,
    async = :true,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-AILabelActions.js",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-AILabelActions.js",
    dynamic = nothing,
    async = :true,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-ExpandableTile.js",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-ExpandableTile.js",
    dynamic = nothing,
    async = :true,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-TabPanel.js",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-TabPanel.js",
    dynamic = nothing,
    async = :true,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-HeaderName.js.map",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-HeaderName.js.map",
    dynamic = true,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-Slider.js.map",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-Slider.js.map",
    dynamic = true,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-TabsVertical.js.map",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-TabsVertical.js.map",
    dynamic = true,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-ErrorBoundaryContext.js.map",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-ErrorBoundaryContext.js.map",
    dynamic = true,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-ButtonSkeleton.js.map",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-ButtonSkeleton.js.map",
    dynamic = true,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-BadgeIndicator.js.map",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-BadgeIndicator.js.map",
    dynamic = true,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-HeaderSideNavItems.js.map",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-HeaderSideNavItems.js.map",
    dynamic = true,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-ProgressIndicatorSkeleton.js.map",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-ProgressIndicatorSkeleton.js.map",
    dynamic = true,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-ToggletipButton.js.map",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-ToggletipButton.js.map",
    dynamic = true,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-NumberInputSkeleton.js.map",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-NumberInputSkeleton.js.map",
    dynamic = true,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-Copy.js.map",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-Copy.js.map",
    dynamic = true,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-ModalWrapper.js.map",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-ModalWrapper.js.map",
    dynamic = true,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-CodeSnippetSkeleton.js.map",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-CodeSnippetSkeleton.js.map",
    dynamic = true,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-MenuItemDivider.js.map",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-MenuItemDivider.js.map",
    dynamic = true,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-BreadcrumbItem.js.map",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-BreadcrumbItem.js.map",
    dynamic = true,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-AILabelContent.js.map",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-AILabelContent.js.map",
    dynamic = true,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-ErrorBoundary.js.map",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-ErrorBoundary.js.map",
    dynamic = true,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-InlineCheckbox.js.map",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-InlineCheckbox.js.map",
    dynamic = true,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-LayoutDirection.js.map",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-LayoutDirection.js.map",
    dynamic = true,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-StructuredListSkeleton.js.map",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-StructuredListSkeleton.js.map",
    dynamic = true,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-ModalFooter.js.map",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-ModalFooter.js.map",
    dynamic = true,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-Plex.js.map",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-Plex.js.map",
    dynamic = true,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-ComposedModal.js.map",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-ComposedModal.js.map",
    dynamic = true,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-RadioButtonSkeleton.js.map",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-RadioButtonSkeleton.js.map",
    dynamic = true,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-ClassPrefix.js.map",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-ClassPrefix.js.map",
    dynamic = true,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-ContextMenu.js.map",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-ContextMenu.js.map",
    dynamic = true,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-TextInput.js.map",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-TextInput.js.map",
    dynamic = true,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-ExpandableSearch.js.map",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-ExpandableSearch.js.map",
    dynamic = true,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-Filename.js.map",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-Filename.js.map",
    dynamic = true,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-TableToolbarContent.js.map",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-TableToolbarContent.js.map",
    dynamic = true,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-FileUploaderDropContainer.js.map",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-FileUploaderDropContainer.js.map",
    dynamic = true,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-SecondaryButton.js.map",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-SecondaryButton.js.map",
    dynamic = true,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-TabContent.js.map",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-TabContent.js.map",
    dynamic = true,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-StructuredListWrapper.js.map",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-StructuredListWrapper.js.map",
    dynamic = true,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-FluidTextInputSkeleton.js.map",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-FluidTextInputSkeleton.js.map",
    dynamic = true,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-FileUploader.js.map",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-FileUploader.js.map",
    dynamic = true,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-FluidDatePicker.js.map",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-FluidDatePicker.js.map",
    dynamic = true,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-Checkbox.js.map",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-Checkbox.js.map",
    dynamic = true,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-SlugActions.js.map",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-SlugActions.js.map",
    dynamic = true,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-Button.js.map",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-Button.js.map",
    dynamic = true,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-MenuItemGroup.js.map",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-MenuItemGroup.js.map",
    dynamic = true,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-SliderSkeleton.js.map",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-SliderSkeleton.js.map",
    dynamic = true,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-SkeletonPlaceholder.js.map",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-SkeletonPlaceholder.js.map",
    dynamic = true,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-NotificationButton.js.map",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-NotificationButton.js.map",
    dynamic = true,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-TableHead.js.map",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-TableHead.js.map",
    dynamic = true,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-ContainedListItem.js.map",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-ContainedListItem.js.map",
    dynamic = true,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-HeaderMenuItem.js.map",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-HeaderMenuItem.js.map",
    dynamic = true,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-DatePickerSkeleton.js.map",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-DatePickerSkeleton.js.map",
    dynamic = true,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-TableToolbarMenu.js.map",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-TableToolbarMenu.js.map",
    dynamic = true,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-ButtonSet.js.map",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-ButtonSet.js.map",
    dynamic = true,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-TableRow.js.map",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-TableRow.js.map",
    dynamic = true,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-PasswordInput.js.map",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-PasswordInput.js.map",
    dynamic = true,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-Icons.js.map",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-Icons.js.map",
    dynamic = true,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-Content.js.map",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-Content.js.map",
    dynamic = true,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-AccordionSkeleton.js.map",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-AccordionSkeleton.js.map",
    dynamic = true,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-TableActionList.js.map",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-TableActionList.js.map",
    dynamic = true,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-CodeSnippet.js.map",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-CodeSnippet.js.map",
    dynamic = true,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-FormLabel.js.map",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-FormLabel.js.map",
    dynamic = true,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-StructuredListHead.js.map",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-StructuredListHead.js.map",
    dynamic = true,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-IconSwitch.js.map",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-IconSwitch.js.map",
    dynamic = true,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-FluidSearch.js.map",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-FluidSearch.js.map",
    dynamic = true,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-Notification.js.map",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-Notification.js.map",
    dynamic = true,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-FluidTimePickerSelect.js.map",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-FluidTimePickerSelect.js.map",
    dynamic = true,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-FluidTimePicker.js.map",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-FluidTimePicker.js.map",
    dynamic = true,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-Dropdown.js.map",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-Dropdown.js.map",
    dynamic = true,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-FormGroup.js.map",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-FormGroup.js.map",
    dynamic = true,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-ToggleSmallSkeleton.js.map",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-ToggleSmallSkeleton.js.map",
    dynamic = true,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-StructuredListRow.js.map",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-StructuredListRow.js.map",
    dynamic = true,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-IconIndicator.js.map",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-IconIndicator.js.map",
    dynamic = true,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-Search.js.map",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-Search.js.map",
    dynamic = true,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-OrderedList.js.map",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-OrderedList.js.map",
    dynamic = true,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-TableExpandedRow.js.map",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-TableExpandedRow.js.map",
    dynamic = true,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-ToggletipContent.js.map",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-ToggletipContent.js.map",
    dynamic = true,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-SideNavFooter.js.map",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-SideNavFooter.js.map",
    dynamic = true,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-TableHeader.js.map",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-TableHeader.js.map",
    dynamic = true,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-IconTab.js.map",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-IconTab.js.map",
    dynamic = true,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-TableToolbarAction.js.map",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-TableToolbarAction.js.map",
    dynamic = true,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-AccordionItem.js.map",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-AccordionItem.js.map",
    dynamic = true,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-OverflowMenuV2.js.map",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-OverflowMenuV2.js.map",
    dynamic = true,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-MenuButton.js.map",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-MenuButton.js.map",
    dynamic = true,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-FluidNumberInputSkeleton.js.map",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-FluidNumberInputSkeleton.js.map",
    dynamic = true,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-Pagination.js.map",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-Pagination.js.map",
    dynamic = true,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-Heading.js.map",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-Heading.js.map",
    dynamic = true,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-MenuItemRadioGroup.js.map",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-MenuItemRadioGroup.js.map",
    dynamic = true,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-Select.js.map",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-Select.js.map",
    dynamic = true,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-SideNavItems.js.map",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-SideNavItems.js.map",
    dynamic = true,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-SideNavLinkText.js.map",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-SideNavLinkText.js.map",
    dynamic = true,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-StaticNotification.js.map",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-StaticNotification.js.map",
    dynamic = true,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-AISkeletonText.js.map",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-AISkeletonText.js.map",
    dynamic = true,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-FormItem.js.map",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-FormItem.js.map",
    dynamic = true,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-ButtonKinds.js.map",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-ButtonKinds.js.map",
    dynamic = true,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-NotificationActionButton.js.map",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-NotificationActionButton.js.map",
    dynamic = true,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-ModalBody.js.map",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-ModalBody.js.map",
    dynamic = true,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-ComposedModalPresence.js.map",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-ComposedModalPresence.js.map",
    dynamic = true,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-NumberInput.js.map",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-NumberInput.js.map",
    dynamic = true,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-SelectItem.js.map",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-SelectItem.js.map",
    dynamic = true,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-ToggleSkeleton.js.map",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-ToggleSkeleton.js.map",
    dynamic = true,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-ProgressIndicator.js.map",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-ProgressIndicator.js.map",
    dynamic = true,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-FluidForm.js.map",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-FluidForm.js.map",
    dynamic = true,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-PrimaryButton.js.map",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-PrimaryButton.js.map",
    dynamic = true,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-PrefixContext.js.map",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-PrefixContext.js.map",
    dynamic = true,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-SkeletonText.js.map",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-SkeletonText.js.map",
    dynamic = true,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-HeaderGlobalAction.js.map",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-HeaderGlobalAction.js.map",
    dynamic = true,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-TabsSkeleton.js.map",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-TabsSkeleton.js.map",
    dynamic = true,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-ChatButtonSkeleton.js.map",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-ChatButtonSkeleton.js.map",
    dynamic = true,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-Tag.js.map",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-Tag.js.map",
    dynamic = true,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-ChatButton.js.map",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-ChatButton.js.map",
    dynamic = true,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-AILabel.js.map",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-AILabel.js.map",
    dynamic = true,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-ListBox.js.map",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-ListBox.js.map",
    dynamic = true,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-InlineNotification.js.map",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-InlineNotification.js.map",
    dynamic = true,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-ProgressStep.js.map",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-ProgressStep.js.map",
    dynamic = true,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-DatePicker.js.map",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-DatePicker.js.map",
    dynamic = true,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-SideNavLink.js.map",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-SideNavLink.js.map",
    dynamic = true,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-ToggletipLabel.js.map",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-ToggletipLabel.js.map",
    dynamic = true,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-FluidSelectSkeleton.js.map",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-FluidSelectSkeleton.js.map",
    dynamic = true,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-SideNavIcon.js.map",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-SideNavIcon.js.map",
    dynamic = true,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-UnorderedList.js.map",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-UnorderedList.js.map",
    dynamic = true,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-TableBatchActions.js.map",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-TableBatchActions.js.map",
    dynamic = true,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-Theme.js.map",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-Theme.js.map",
    dynamic = true,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-DataTable.js.map",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-DataTable.js.map",
    dynamic = true,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-RadioButtonGroup.js.map",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-RadioButtonGroup.js.map",
    dynamic = true,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-FluidSelect.js.map",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-FluidSelect.js.map",
    dynamic = true,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-Tabs.js.map",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-Tabs.js.map",
    dynamic = true,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-TableSelectRow.js.map",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-TableSelectRow.js.map",
    dynamic = true,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-HeaderMenu.js.map",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-HeaderMenu.js.map",
    dynamic = true,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-Callout.js.map",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-Callout.js.map",
    dynamic = true,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-ComboButton.js.map",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-ComboButton.js.map",
    dynamic = true,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-Icon.js.map",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-Icon.js.map",
    dynamic = true,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-Link.js.map",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-Link.js.map",
    dynamic = true,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-Tile.js.map",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-Tile.js.map",
    dynamic = true,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-FluidDropdown.js.map",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-FluidDropdown.js.map",
    dynamic = true,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-InlineLoading.js.map",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-InlineLoading.js.map",
    dynamic = true,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-TableToolbar.js.map",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-TableToolbar.js.map",
    dynamic = true,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-AspectRatio.js.map",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-AspectRatio.js.map",
    dynamic = true,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-IconSkeleton.js.map",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-IconSkeleton.js.map",
    dynamic = true,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-DismissibleTag.js.map",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-DismissibleTag.js.map",
    dynamic = true,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-BreadcrumbSkeleton.js.map",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-BreadcrumbSkeleton.js.map",
    dynamic = true,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-ClickableTile.js.map",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-ClickableTile.js.map",
    dynamic = true,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-SelectableTile.js.map",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-SelectableTile.js.map",
    dynamic = true,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-GridSettings.js.map",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-GridSettings.js.map",
    dynamic = true,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-MenuItemSelectable.js.map",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-MenuItemSelectable.js.map",
    dynamic = true,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-Grid.js.map",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-Grid.js.map",
    dynamic = true,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-ButtonSizes.js.map",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-ButtonSizes.js.map",
    dynamic = true,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-Tab.js.map",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-Tab.js.map",
    dynamic = true,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-MenuItem.js.map",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-MenuItem.js.map",
    dynamic = true,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-ProgressBar.js.map",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-ProgressBar.js.map",
    dynamic = true,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-SideNavDetails.js.map",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-SideNavDetails.js.map",
    dynamic = true,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-FluidMultiSelect.js.map",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-FluidMultiSelect.js.map",
    dynamic = true,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-SelectSkeleton.js.map",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-SelectSkeleton.js.map",
    dynamic = true,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-Row.js.map",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-Row.js.map",
    dynamic = true,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-TimePickerSelect.js.map",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-TimePickerSelect.js.map",
    dynamic = true,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-TimePicker.js.map",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-TimePicker.js.map",
    dynamic = true,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-FluidComboBoxSkeleton.js.map",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-FluidComboBoxSkeleton.js.map",
    dynamic = true,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-SideNavMenuItem.js.map",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-SideNavMenuItem.js.map",
    dynamic = true,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-Popover.js.map",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-Popover.js.map",
    dynamic = true,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-Column.js.map",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-Column.js.map",
    dynamic = true,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-OperationalTag.js.map",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-OperationalTag.js.map",
    dynamic = true,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-ThemeContext.js.map",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-ThemeContext.js.map",
    dynamic = true,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-FluidNumberInput.js.map",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-FluidNumberInput.js.map",
    dynamic = true,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-PageHeader.js.map",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-PageHeader.js.map",
    dynamic = true,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-CarbonDash.js.map",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-CarbonDash.js.map",
    dynamic = true,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-ModalHeader.js.map",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-ModalHeader.js.map",
    dynamic = true,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-Slug.js.map",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-Slug.js.map",
    dynamic = true,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-FilterableMultiSelect.js.map",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-FilterableMultiSelect.js.map",
    dynamic = true,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-Toggle.js.map",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-Toggle.js.map",
    dynamic = true,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-TableSlugRow.js.map",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-TableSlugRow.js.map",
    dynamic = true,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-AISkeletonPlaceholder.js.map",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-AISkeletonPlaceholder.js.map",
    dynamic = true,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-ActionableNotification.js.map",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-ActionableNotification.js.map",
    dynamic = true,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-UIShell.js.map",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-UIShell.js.map",
    dynamic = true,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-OverflowMenuItem.js.map",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-OverflowMenuItem.js.map",
    dynamic = true,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-FluidDropdownSkeleton.js.map",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-FluidDropdownSkeleton.js.map",
    dynamic = true,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-Switcher.js.map",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-Switcher.js.map",
    dynamic = true,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-RadioTile.js.map",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-RadioTile.js.map",
    dynamic = true,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-FluidDatePickerInput.js.map",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-FluidDatePickerInput.js.map",
    dynamic = true,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-ModalPresence.js.map",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-ModalPresence.js.map",
    dynamic = true,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-HeaderNavigation.js.map",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-HeaderNavigation.js.map",
    dynamic = true,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-SkipToContent.js.map",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-SkipToContent.js.map",
    dynamic = true,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-ToastNotification.js.map",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-ToastNotification.js.map",
    dynamic = true,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-FluidMultiSelectSkeleton.js.map",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-FluidMultiSelectSkeleton.js.map",
    dynamic = true,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-HeaderMenuButton.js.map",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-HeaderMenuButton.js.map",
    dynamic = true,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-TabListVertical.js.map",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-TabListVertical.js.map",
    dynamic = true,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-TreeNode.js.map",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-TreeNode.js.map",
    dynamic = true,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-TableDecoratorRow.js.map",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-TableDecoratorRow.js.map",
    dynamic = true,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-SideNavSwitcher.js.map",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-SideNavSwitcher.js.map",
    dynamic = true,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-RadioButton.js.map",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-RadioButton.js.map",
    dynamic = true,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-FluidTextArea.js.map",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-FluidTextArea.js.map",
    dynamic = true,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-SideNavHeader.js.map",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-SideNavHeader.js.map",
    dynamic = true,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-HeaderGlobalBar.js.map",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-HeaderGlobalBar.js.map",
    dynamic = true,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-TileAboveTheFoldContent.js.map",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-TileAboveTheFoldContent.js.map",
    dynamic = true,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-Portal.js.map",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-Portal.js.map",
    dynamic = true,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-TableBody.js.map",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-TableBody.js.map",
    dynamic = true,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-PaginationNav.js.map",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-PaginationNav.js.map",
    dynamic = true,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-SideNavItem.js.map",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-SideNavItem.js.map",
    dynamic = true,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-Disclosure.js.map",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-Disclosure.js.map",
    dynamic = true,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-Table.js.map",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-Table.js.map",
    dynamic = true,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-TileBelowTheFoldContent.js.map",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-TileBelowTheFoldContent.js.map",
    dynamic = true,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-VStack.js.map",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-VStack.js.map",
    dynamic = true,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-CheckboxGroup.js.map",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-CheckboxGroup.js.map",
    dynamic = true,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-StructuredListBody.js.map",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-StructuredListBody.js.map",
    dynamic = true,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-FluidComboBox.js.map",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-FluidComboBox.js.map",
    dynamic = true,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-Loading.js.map",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-Loading.js.map",
    dynamic = true,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-DataTableSkeleton.js.map",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-DataTableSkeleton.js.map",
    dynamic = true,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-StructuredListInput.js.map",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-StructuredListInput.js.map",
    dynamic = true,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-ButtonTooltipAlignments.js.map",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-ButtonTooltipAlignments.js.map",
    dynamic = true,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-IdPrefix.js.map",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-IdPrefix.js.map",
    dynamic = true,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-SelectableTag.js.map",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-SelectableTag.js.map",
    dynamic = true,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-PopoverContent.js.map",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-PopoverContent.js.map",
    dynamic = true,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-Dialog.js.map",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-Dialog.js.map",
    dynamic = true,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-ContainedList.js.map",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-ContainedList.js.map",
    dynamic = true,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-MultiSelect.js.map",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-MultiSelect.js.map",
    dynamic = true,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-FluidTextAreaSkeleton.js.map",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-FluidTextAreaSkeleton.js.map",
    dynamic = true,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-SideNavDivider.js.map",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-SideNavDivider.js.map",
    dynamic = true,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-TableExpandHeader.js.map",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-TableExpandHeader.js.map",
    dynamic = true,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-PaginationSkeleton.js.map",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-PaginationSkeleton.js.map",
    dynamic = true,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-SwitcherItem.js.map",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-SwitcherItem.js.map",
    dynamic = true,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-Header.js.map",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-Header.js.map",
    dynamic = true,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-AISkeleton.js.map",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-AISkeleton.js.map",
    dynamic = true,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-DangerButton.js.map",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-DangerButton.js.map",
    dynamic = true,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-TileGroup.js.map",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-TileGroup.js.map",
    dynamic = true,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-TabList.js.map",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-TabList.js.map",
    dynamic = true,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-SideNav.js.map",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-SideNav.js.map",
    dynamic = true,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-ToggleSmall.js.map",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-ToggleSmall.js.map",
    dynamic = true,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-TableBatchAction.js.map",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-TableBatchAction.js.map",
    dynamic = true,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-ShapeIndicator.js.map",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-ShapeIndicator.js.map",
    dynamic = true,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-DefinitionTooltip.js.map",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-DefinitionTooltip.js.map",
    dynamic = true,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-TreeView.js.map",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-TreeView.js.map",
    dynamic = true,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-GlobalTheme.js.map",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-GlobalTheme.js.map",
    dynamic = true,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-Tooltip.js.map",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-Tooltip.js.map",
    dynamic = true,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-ControlledPasswordInput.js.map",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-ControlledPasswordInput.js.map",
    dynamic = true,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-OverflowMenu.js.map",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-OverflowMenu.js.map",
    dynamic = true,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-TableCell.js.map",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-TableCell.js.map",
    dynamic = true,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-IconButton.js.map",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-IconButton.js.map",
    dynamic = true,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-Section.js.map",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-Section.js.map",
    dynamic = true,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-FluidDatePickerSkeleton.js.map",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-FluidDatePickerSkeleton.js.map",
    dynamic = true,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-Layout.js.map",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-Layout.js.map",
    dynamic = true,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-TagSkeleton.js.map",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-TagSkeleton.js.map",
    dynamic = true,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-ToggletipActions.js.map",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-ToggletipActions.js.map",
    dynamic = true,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-FileUploaderItem.js.map",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-FileUploaderItem.js.map",
    dynamic = true,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-Stack.js.map",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-Stack.js.map",
    dynamic = true,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-Text.js.map",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-Text.js.map",
    dynamic = true,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-StructuredListCell.js.map",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-StructuredListCell.js.map",
    dynamic = true,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-ContentSwitcher.js.map",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-ContentSwitcher.js.map",
    dynamic = true,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-TextInputSkeleton.js.map",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-TextInputSkeleton.js.map",
    dynamic = true,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-FileUploaderButton.js.map",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-FileUploaderButton.js.map",
    dynamic = true,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-DatePickerInput.js.map",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-DatePickerInput.js.map",
    dynamic = true,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-Toggletip.js.map",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-Toggletip.js.map",
    dynamic = true,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-FluidTimePickerSkeleton.js.map",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-FluidTimePickerSkeleton.js.map",
    dynamic = true,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-CheckboxSkeleton.js.map",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-CheckboxSkeleton.js.map",
    dynamic = true,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-IconButtonKinds.js.map",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-IconButtonKinds.js.map",
    dynamic = true,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-ButtonTooltipPositions.js.map",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-ButtonTooltipPositions.js.map",
    dynamic = true,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-HeaderPanel.js.map",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-HeaderPanel.js.map",
    dynamic = true,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-FileUploaderSkeleton.js.map",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-FileUploaderSkeleton.js.map",
    dynamic = true,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-Modal.js.map",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-Modal.js.map",
    dynamic = true,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-FluidSearchSkeleton.js.map",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-FluidSearchSkeleton.js.map",
    dynamic = true,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-HStack.js.map",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-HStack.js.map",
    dynamic = true,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-FluidTextInput.js.map",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-FluidTextInput.js.map",
    dynamic = true,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-DropdownSkeleton.js.map",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-DropdownSkeleton.js.map",
    dynamic = true,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-Accordion.js.map",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-Accordion.js.map",
    dynamic = true,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-SideNavMenu.js.map",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-SideNavMenu.js.map",
    dynamic = true,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-TableExpandRow.js.map",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-TableExpandRow.js.map",
    dynamic = true,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-Layer.js.map",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-Layer.js.map",
    dynamic = true,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-SkeletonIcon.js.map",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-SkeletonIcon.js.map",
    dynamic = true,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-TextAreaSkeleton.js.map",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-TextAreaSkeleton.js.map",
    dynamic = true,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-SwitcherDivider.js.map",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-SwitcherDivider.js.map",
    dynamic = true,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-FlexGrid.js.map",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-FlexGrid.js.map",
    dynamic = true,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-Breadcrumb.js.map",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-Breadcrumb.js.map",
    dynamic = true,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-AISkeletonIcon.js.map",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-AISkeletonIcon.js.map",
    dynamic = true,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-StructuredList.js.map",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-StructuredList.js.map",
    dynamic = true,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-FluidPasswordInput.js.map",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-FluidPasswordInput.js.map",
    dynamic = true,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-HeaderContainer.js.map",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-HeaderContainer.js.map",
    dynamic = true,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-SlugContent.js.map",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-SlugContent.js.map",
    dynamic = true,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-TabPanels.js.map",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-TabPanels.js.map",
    dynamic = true,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-Menu.js.map",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-Menu.js.map",
    dynamic = true,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-Switch.js.map",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-Switch.js.map",
    dynamic = true,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-CopyButton.js.map",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-CopyButton.js.map",
    dynamic = true,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-Form.js.map",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-Form.js.map",
    dynamic = true,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-ColumnHang.js.map",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-ColumnHang.js.map",
    dynamic = true,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-FeatureFlags.js.map",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-FeatureFlags.js.map",
    dynamic = true,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-FormContext.js.map",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-FormContext.js.map",
    dynamic = true,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-TextArea.js.map",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-TextArea.js.map",
    dynamic = true,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-TableContainer.js.map",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-TableContainer.js.map",
    dynamic = true,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-ComboBox.js.map",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-ComboBox.js.map",
    dynamic = true,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-ListItem.js.map",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-ListItem.js.map",
    dynamic = true,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-TableToolbarSearch.js.map",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-TableToolbarSearch.js.map",
    dynamic = true,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-SearchSkeleton.js.map",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-SearchSkeleton.js.map",
    dynamic = true,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-SelectItemGroup.js.map",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-SelectItemGroup.js.map",
    dynamic = true,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-TableSelectAll.js.map",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-TableSelectAll.js.map",
    dynamic = true,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-HideAtBreakpoint.js.map",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-HideAtBreakpoint.js.map",
    dynamic = true,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-AILabelActions.js.map",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-AILabelActions.js.map",
    dynamic = true,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-ExpandableTile.js.map",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-ExpandableTile.js.map",
    dynamic = true,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-TabPanel.js.map",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-TabPanel.js.map",
    dynamic = true,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "carbon_dash.min.js",
    external_url = nothing,
    dynamic = nothing,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "carbon_dash.min.js.map",
    external_url = nothing,
    dynamic = true,
    async = nothing,
    type = :js
)
            ]
        )

    )
end
end
