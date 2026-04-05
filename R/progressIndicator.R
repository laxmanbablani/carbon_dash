# AUTO GENERATED FILE - DO NOT EDIT

#' @export
progressIndicator <- function(children=NULL, id=NULL, className=NULL, currentIndex=NULL, loading_state=NULL, onChange=NULL, spaceEqually=NULL, style=NULL, vertical=NULL) {
    
    props <- list(children=children, id=id, className=className, currentIndex=currentIndex, loading_state=loading_state, onChange=onChange, spaceEqually=spaceEqually, style=style, vertical=vertical)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'ProgressIndicator',
        namespace = 'carbon_dash',
        propNames = c('children', 'id', 'className', 'currentIndex', 'loading_state', 'onChange', 'spaceEqually', 'style', 'vertical'),
        package = 'carbonDash'
        )

    structure(component, class = c('dash_component', 'list'))
}
