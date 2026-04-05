# AUTO GENERATED FILE - DO NOT EDIT

#' @export
accordionSkeleton <- function(children=NULL, id=NULL, align=NULL, className=NULL, count=NULL, isFlush=NULL, loading_state=NULL, open=NULL, ordered=NULL, style=NULL) {
    
    props <- list(children=children, id=id, align=align, className=className, count=count, isFlush=isFlush, loading_state=loading_state, open=open, ordered=ordered, style=style)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'AccordionSkeleton',
        namespace = 'carbon_dash',
        propNames = c('children', 'id', 'align', 'className', 'count', 'isFlush', 'loading_state', 'open', 'ordered', 'style'),
        package = 'carbonDash'
        )

    structure(component, class = c('dash_component', 'list'))
}
