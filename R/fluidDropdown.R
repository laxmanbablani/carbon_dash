# AUTO GENERATED FILE - DO NOT EDIT

#' @export
fluidDropdown <- function(children=NULL, id=NULL, className=NULL, direction=NULL, disabled=NULL, initialSelectedItem=NULL, invalid=NULL, invalidText=NULL, isCondensed=NULL, itemToElement=NULL, itemToString=NULL, items=NULL, label=NULL, loading_state=NULL, onChange=NULL, renderSelectedItem=NULL, selectedItem=NULL, style=NULL, titleText=NULL, translateWithId=NULL, warn=NULL, warnText=NULL) {
    
    props <- list(children=children, id=id, className=className, direction=direction, disabled=disabled, initialSelectedItem=initialSelectedItem, invalid=invalid, invalidText=invalidText, isCondensed=isCondensed, itemToElement=itemToElement, itemToString=itemToString, items=items, label=label, loading_state=loading_state, onChange=onChange, renderSelectedItem=renderSelectedItem, selectedItem=selectedItem, style=style, titleText=titleText, translateWithId=translateWithId, warn=warn, warnText=warnText)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'FluidDropdown',
        namespace = 'carbon_dash',
        propNames = c('children', 'id', 'className', 'direction', 'disabled', 'initialSelectedItem', 'invalid', 'invalidText', 'isCondensed', 'itemToElement', 'itemToString', 'items', 'label', 'loading_state', 'onChange', 'renderSelectedItem', 'selectedItem', 'style', 'titleText', 'translateWithId', 'warn', 'warnText'),
        package = 'carbonDash'
        )

    structure(component, class = c('dash_component', 'list'))
}
