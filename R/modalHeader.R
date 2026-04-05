# AUTO GENERATED FILE - DO NOT EDIT

#' @export
modalHeader <- function(children=NULL, id=NULL, buttonOnClick=NULL, className=NULL, closeClassName=NULL, closeIconClassName=NULL, closeModal=NULL, iconDescription=NULL, label=NULL, labelClassName=NULL, loading_state=NULL, style=NULL, title=NULL, titleClassName=NULL) {
    
    props <- list(children=children, id=id, buttonOnClick=buttonOnClick, className=className, closeClassName=closeClassName, closeIconClassName=closeIconClassName, closeModal=closeModal, iconDescription=iconDescription, label=label, labelClassName=labelClassName, loading_state=loading_state, style=style, title=title, titleClassName=titleClassName)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'ModalHeader',
        namespace = 'carbon_dash',
        propNames = c('children', 'id', 'buttonOnClick', 'className', 'closeClassName', 'closeIconClassName', 'closeModal', 'iconDescription', 'label', 'labelClassName', 'loading_state', 'style', 'title', 'titleClassName'),
        package = 'carbonDash'
        )

    structure(component, class = c('dash_component', 'list'))
}
