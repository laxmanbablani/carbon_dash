# AUTO GENERATED FILE - DO NOT EDIT

#' @export
sideNavSwitcher <- function(children=NULL, id=NULL, className=NULL, labelText=NULL, loading_state=NULL, onChange=NULL, options=NULL, style=NULL) {
    
    props <- list(children=children, id=id, className=className, labelText=labelText, loading_state=loading_state, onChange=onChange, options=options, style=style)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'SideNavSwitcher',
        namespace = 'carbon_dash',
        propNames = c('children', 'id', 'className', 'labelText', 'loading_state', 'onChange', 'options', 'style'),
        package = 'carbonDash'
        )

    structure(component, class = c('dash_component', 'list'))
}
