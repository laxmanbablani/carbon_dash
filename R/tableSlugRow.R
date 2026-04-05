# AUTO GENERATED FILE - DO NOT EDIT

#' @export
tableSlugRow <- function(children=NULL, id=NULL, className=NULL, loading_state=NULL, slug=NULL, style=NULL) {
    
    props <- list(children=children, id=id, className=className, loading_state=loading_state, slug=slug, style=style)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'TableSlugRow',
        namespace = 'carbon_dash',
        propNames = c('children', 'id', 'className', 'loading_state', 'slug', 'style'),
        package = 'carbonDash'
        )

    structure(component, class = c('dash_component', 'list'))
}
