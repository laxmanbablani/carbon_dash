# AUTO GENERATED FILE - DO NOT EDIT

#' @export
modalBody <- function(children=NULL, id=NULL, className=NULL, hasForm=NULL, hasScrollingContent=NULL, loading_state=NULL, style=NULL) {
    
    props <- list(children=children, id=id, className=className, hasForm=hasForm, hasScrollingContent=hasScrollingContent, loading_state=loading_state, style=style)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'ModalBody',
        namespace = 'carbon_dash',
        propNames = c('children', 'id', 'className', 'hasForm', 'hasScrollingContent', 'loading_state', 'style'),
        package = 'carbonDash'
        )

    structure(component, class = c('dash_component', 'list'))
}
