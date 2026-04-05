# AUTO GENERATED FILE - DO NOT EDIT

#' @export
buttonSet <- function(children=NULL, id=NULL, className=NULL, fluid=NULL, loading_state=NULL, stacked=NULL, style=NULL) {
    
    props <- list(children=children, id=id, className=className, fluid=fluid, loading_state=loading_state, stacked=stacked, style=style)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'ButtonSet',
        namespace = 'carbon_dash',
        propNames = c('children', 'id', 'className', 'fluid', 'loading_state', 'stacked', 'style'),
        package = 'carbonDash'
        )

    structure(component, class = c('dash_component', 'list'))
}
