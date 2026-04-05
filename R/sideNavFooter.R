# AUTO GENERATED FILE - DO NOT EDIT

#' @export
sideNavFooter <- function(children=NULL, id=NULL, assistiveText=NULL, className=NULL, expanded=NULL, loading_state=NULL, onToggle=NULL, style=NULL) {
    
    props <- list(children=children, id=id, assistiveText=assistiveText, className=className, expanded=expanded, loading_state=loading_state, onToggle=onToggle, style=style)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'SideNavFooter',
        namespace = 'carbon_dash',
        propNames = c('children', 'id', 'assistiveText', 'className', 'expanded', 'loading_state', 'onToggle', 'style'),
        package = 'carbonDash'
        )

    structure(component, class = c('dash_component', 'list'))
}
