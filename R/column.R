# AUTO GENERATED FILE - DO NOT EDIT

#' @export
column <- function(children=NULL, id=NULL, as_=NULL, className=NULL, lg=NULL, loading_state=NULL, max=NULL, md=NULL, sm=NULL, span=NULL, style=NULL, xlg=NULL) {
    
    props <- list(children=children, id=id, as_=as_, className=className, lg=lg, loading_state=loading_state, max=max, md=md, sm=sm, span=span, style=style, xlg=xlg)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'Column',
        namespace = 'carbon_dash',
        propNames = c('children', 'id', 'as_', 'className', 'lg', 'loading_state', 'max', 'md', 'sm', 'span', 'style', 'xlg'),
        package = 'carbonDash'
        )

    structure(component, class = c('dash_component', 'list'))
}
