# AUTO GENERATED FILE - DO NOT EDIT

#' @export
menuItemSelectable <- function(children=NULL, id=NULL, className=NULL, defaultSelected=NULL, label=NULL, loading_state=NULL, onChange=NULL, selected=NULL, style=NULL) {
    
    props <- list(children=children, id=id, className=className, defaultSelected=defaultSelected, label=label, loading_state=loading_state, onChange=onChange, selected=selected, style=style)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'MenuItemSelectable',
        namespace = 'carbon_dash',
        propNames = c('children', 'id', 'className', 'defaultSelected', 'label', 'loading_state', 'onChange', 'selected', 'style'),
        package = 'carbonDash'
        )

    structure(component, class = c('dash_component', 'list'))
}
