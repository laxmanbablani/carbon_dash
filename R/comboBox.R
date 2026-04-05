# AUTO GENERATED FILE - DO NOT EDIT

#' @export
comboBox <- function(children=NULL, id=NULL, allowCustomValue=NULL, ariaLabel=NULL, autoAlign=NULL, className=NULL, decorator=NULL, direction=NULL, disabled=NULL, downshiftActions=NULL, downshiftProps=NULL, helperText=NULL, initialSelectedItem=NULL, inputProps=NULL, invalid=NULL, invalidText=NULL, itemToElement=NULL, itemToString=NULL, items=NULL, light=NULL, loading_state=NULL, onChange=NULL, onInputChange=NULL, onToggleClick=NULL, placeholder=NULL, readOnly=NULL, selectedItem=NULL, shouldFilterItem=NULL, size=NULL, slug=NULL, style=NULL, titleText=NULL, translateWithId=NULL, typeahead=NULL, warn=NULL, warnText=NULL) {
    
    props <- list(children=children, id=id, allowCustomValue=allowCustomValue, ariaLabel=ariaLabel, autoAlign=autoAlign, className=className, decorator=decorator, direction=direction, disabled=disabled, downshiftActions=downshiftActions, downshiftProps=downshiftProps, helperText=helperText, initialSelectedItem=initialSelectedItem, inputProps=inputProps, invalid=invalid, invalidText=invalidText, itemToElement=itemToElement, itemToString=itemToString, items=items, light=light, loading_state=loading_state, onChange=onChange, onInputChange=onInputChange, onToggleClick=onToggleClick, placeholder=placeholder, readOnly=readOnly, selectedItem=selectedItem, shouldFilterItem=shouldFilterItem, size=size, slug=slug, style=style, titleText=titleText, translateWithId=translateWithId, typeahead=typeahead, warn=warn, warnText=warnText)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'ComboBox',
        namespace = 'carbon_dash',
        propNames = c('children', 'id', 'allowCustomValue', 'ariaLabel', 'autoAlign', 'className', 'decorator', 'direction', 'disabled', 'downshiftActions', 'downshiftProps', 'helperText', 'initialSelectedItem', 'inputProps', 'invalid', 'invalidText', 'itemToElement', 'itemToString', 'items', 'light', 'loading_state', 'onChange', 'onInputChange', 'onToggleClick', 'placeholder', 'readOnly', 'selectedItem', 'shouldFilterItem', 'size', 'slug', 'style', 'titleText', 'translateWithId', 'typeahead', 'warn', 'warnText'),
        package = 'carbonDash'
        )

    structure(component, class = c('dash_component', 'list'))
}
