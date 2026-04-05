# AUTO GENERATED FILE - DO NOT EDIT

#' @export
tile <- function(children=NULL, id=NULL, className=NULL, decorator=NULL, hasRoundedCorners=NULL, light=NULL, loading_state=NULL, slug=NULL, style=NULL) {
    
    props <- list(children=children, id=id, className=className, decorator=decorator, hasRoundedCorners=hasRoundedCorners, light=light, loading_state=loading_state, slug=slug, style=style)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'Tile',
        namespace = 'carbon_dash',
        propNames = c('children', 'id', 'className', 'decorator', 'hasRoundedCorners', 'light', 'loading_state', 'slug', 'style'),
        package = 'carbonDash'
        )

    structure(component, class = c('dash_component', 'list'))
}
