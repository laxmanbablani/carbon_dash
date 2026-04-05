# AUTO GENERATED FILE - DO NOT EDIT

#' @export
accordion <- function(children=NULL, id=NULL, align=NULL, className=NULL, disabled=NULL, isFlush=NULL, loading_state=NULL, ordered=NULL, size=NULL, style=NULL) {
    
    props <- list(children=children, id=id, align=align, className=className, disabled=disabled, isFlush=isFlush, loading_state=loading_state, ordered=ordered, size=size, style=style)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'Accordion',
        namespace = 'carbon_dash',
        propNames = c('children', 'id', 'align', 'className', 'disabled', 'isFlush', 'loading_state', 'ordered', 'size', 'style'),
        package = 'carbonDash'
        )

    structure(component, class = c('dash_component', 'list'))
}
