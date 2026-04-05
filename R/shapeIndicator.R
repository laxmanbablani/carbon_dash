# AUTO GENERATED FILE - DO NOT EDIT

#' @export
shapeIndicator <- function(children=NULL, id=NULL, className=NULL, kind=NULL, label=NULL, loading_state=NULL, style=NULL, textSize=NULL) {
    
    props <- list(children=children, id=id, className=className, kind=kind, label=label, loading_state=loading_state, style=style, textSize=textSize)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'ShapeIndicator',
        namespace = 'carbon_dash',
        propNames = c('children', 'id', 'className', 'kind', 'label', 'loading_state', 'style', 'textSize'),
        package = 'carbonDash'
        )

    structure(component, class = c('dash_component', 'list'))
}
