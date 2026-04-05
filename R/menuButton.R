# AUTO GENERATED FILE - DO NOT EDIT

#' @export
menuButton <- function(children=NULL, id=NULL, className=NULL, disabled=NULL, kind=NULL, label=NULL, loading_state=NULL, menuAlignment=NULL, menuBackgroundToken=NULL, menuBorder=NULL, menuTarget=NULL, size=NULL, style=NULL, tabIndex=NULL) {
    
    props <- list(children=children, id=id, className=className, disabled=disabled, kind=kind, label=label, loading_state=loading_state, menuAlignment=menuAlignment, menuBackgroundToken=menuBackgroundToken, menuBorder=menuBorder, menuTarget=menuTarget, size=size, style=style, tabIndex=tabIndex)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'MenuButton',
        namespace = 'carbon_dash',
        propNames = c('children', 'id', 'className', 'disabled', 'kind', 'label', 'loading_state', 'menuAlignment', 'menuBackgroundToken', 'menuBorder', 'menuTarget', 'size', 'style', 'tabIndex'),
        package = 'carbonDash'
        )

    structure(component, class = c('dash_component', 'list'))
}
