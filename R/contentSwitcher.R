# AUTO GENERATED FILE - DO NOT EDIT

#' @export
contentSwitcher <- function(children=NULL, id=NULL, className=NULL, light=NULL, loading_state=NULL, lowContrast=NULL, onChange=NULL, selectedIndex=NULL, selectionMode=NULL, size=NULL, style=NULL) {
    
    props <- list(children=children, id=id, className=className, light=light, loading_state=loading_state, lowContrast=lowContrast, onChange=onChange, selectedIndex=selectedIndex, selectionMode=selectionMode, size=size, style=style)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'ContentSwitcher',
        namespace = 'carbon_dash',
        propNames = c('children', 'id', 'className', 'light', 'loading_state', 'lowContrast', 'onChange', 'selectedIndex', 'selectionMode', 'size', 'style'),
        package = 'carbonDash'
        )

    structure(component, class = c('dash_component', 'list'))
}
