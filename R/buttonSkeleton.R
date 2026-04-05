# AUTO GENERATED FILE - DO NOT EDIT

#' @export
buttonSkeleton <- function(children=NULL, id=NULL, className=NULL, href=NULL, loading_state=NULL, size=NULL, small=NULL, style=NULL) {
    
    props <- list(children=children, id=id, className=className, href=href, loading_state=loading_state, size=size, small=small, style=style)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'ButtonSkeleton',
        namespace = 'carbon_dash',
        propNames = c('children', 'id', 'className', 'href', 'loading_state', 'size', 'small', 'style'),
        package = 'carbonDash'
        )

    structure(component, class = c('dash_component', 'list'))
}
