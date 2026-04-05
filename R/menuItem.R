# AUTO GENERATED FILE - DO NOT EDIT

#' @export
menuItem <- function(children=NULL, id=NULL, className=NULL, dangerDescription=NULL, disabled=NULL, kind=NULL, label=NULL, loading_state=NULL, onClick=NULL, renderIcon=NULL, shortcut=NULL, style=NULL) {
    
    props <- list(children=children, id=id, className=className, dangerDescription=dangerDescription, disabled=disabled, kind=kind, label=label, loading_state=loading_state, onClick=onClick, renderIcon=renderIcon, shortcut=shortcut, style=style)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'MenuItem',
        namespace = 'carbon_dash',
        propNames = c('children', 'id', 'className', 'dangerDescription', 'disabled', 'kind', 'label', 'loading_state', 'onClick', 'renderIcon', 'shortcut', 'style'),
        package = 'carbonDash'
        )

    structure(component, class = c('dash_component', 'list'))
}
