# AUTO GENERATED FILE - DO NOT EDIT

#' @export
dropdown <- function(children=NULL, id=NULL, ariaLabel=NULL, autoAlign=NULL, className=NULL, decorator=NULL, direction=NULL, disabled=NULL, downshiftProps=NULL, helperText=NULL, hideLabel=NULL, initialSelectedItem=NULL, invalid=NULL, invalidText=NULL, itemToElement=NULL, itemToString=NULL, items=NULL, label=NULL, light=NULL, loading_state=NULL, onChange=NULL, persisted_props=NULL, persistence=NULL, persistence_type=NULL, readOnly=NULL, renderSelectedItem=NULL, selectedItem=NULL, size=NULL, slug=NULL, style=NULL, title=NULL, titleText=NULL, translateWithId=NULL, type=NULL, warn=NULL, warnText=NULL) {
    
    props <- list(children=children, id=id, ariaLabel=ariaLabel, autoAlign=autoAlign, className=className, decorator=decorator, direction=direction, disabled=disabled, downshiftProps=downshiftProps, helperText=helperText, hideLabel=hideLabel, initialSelectedItem=initialSelectedItem, invalid=invalid, invalidText=invalidText, itemToElement=itemToElement, itemToString=itemToString, items=items, label=label, light=light, loading_state=loading_state, onChange=onChange, persisted_props=persisted_props, persistence=persistence, persistence_type=persistence_type, readOnly=readOnly, renderSelectedItem=renderSelectedItem, selectedItem=selectedItem, size=size, slug=slug, style=style, title=title, titleText=titleText, translateWithId=translateWithId, type=type, warn=warn, warnText=warnText)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'Dropdown',
        namespace = 'carbon_dash',
        propNames = c('children', 'id', 'ariaLabel', 'autoAlign', 'className', 'decorator', 'direction', 'disabled', 'downshiftProps', 'helperText', 'hideLabel', 'initialSelectedItem', 'invalid', 'invalidText', 'itemToElement', 'itemToString', 'items', 'label', 'light', 'loading_state', 'onChange', 'persisted_props', 'persistence', 'persistence_type', 'readOnly', 'renderSelectedItem', 'selectedItem', 'size', 'slug', 'style', 'title', 'titleText', 'translateWithId', 'type', 'warn', 'warnText'),
        package = 'carbonDash'
        )

    structure(component, class = c('dash_component', 'list'))
}
