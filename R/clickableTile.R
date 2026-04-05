# AUTO GENERATED FILE - DO NOT EDIT

#' @export
clickableTile <- function(children=NULL, id=NULL, className=NULL, clicked=NULL, decorator=NULL, disabled=NULL, hasRoundedCorners=NULL, href=NULL, light=NULL, loading_state=NULL, onClick=NULL, onKeyDown=NULL, rel=NULL, renderIcon=NULL, style=NULL) {
    
    props <- list(children=children, id=id, className=className, clicked=clicked, decorator=decorator, disabled=disabled, hasRoundedCorners=hasRoundedCorners, href=href, light=light, loading_state=loading_state, onClick=onClick, onKeyDown=onKeyDown, rel=rel, renderIcon=renderIcon, style=style)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'ClickableTile',
        namespace = 'carbon_dash',
        propNames = c('children', 'id', 'className', 'clicked', 'decorator', 'disabled', 'hasRoundedCorners', 'href', 'light', 'loading_state', 'onClick', 'onKeyDown', 'rel', 'renderIcon', 'style'),
        package = 'carbonDash'
        )

    structure(component, class = c('dash_component', 'list'))
}
