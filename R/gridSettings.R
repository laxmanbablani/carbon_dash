# AUTO GENERATED FILE - DO NOT EDIT

#' @export
gridSettings <- function(children=NULL, id=NULL, className=NULL, loading_state=NULL, mode=NULL, style=NULL, subgrid=NULL) {
    
    props <- list(children=children, id=id, className=className, loading_state=loading_state, mode=mode, style=style, subgrid=subgrid)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'GridSettings',
        namespace = 'carbon_dash',
        propNames = c('children', 'id', 'className', 'loading_state', 'mode', 'style', 'subgrid'),
        package = 'carbonDash'
        )

    structure(component, class = c('dash_component', 'list'))
}
