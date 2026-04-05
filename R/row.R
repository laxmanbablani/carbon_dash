# AUTO GENERATED FILE - DO NOT EDIT

#' @export
row <- function(children=NULL, id=NULL, as_=NULL, className=NULL, condensed=NULL, loading_state=NULL, narrow=NULL, style=NULL) {
    
    props <- list(children=children, id=id, as_=as_, className=className, condensed=condensed, loading_state=loading_state, narrow=narrow, style=style)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'Row',
        namespace = 'carbon_dash',
        propNames = c('children', 'id', 'as_', 'className', 'condensed', 'loading_state', 'narrow', 'style'),
        package = 'carbonDash'
        )

    structure(component, class = c('dash_component', 'list'))
}
