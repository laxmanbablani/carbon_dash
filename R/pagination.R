# AUTO GENERATED FILE - DO NOT EDIT

#' @export
pagination <- function(children=NULL, id=NULL, backwardText=NULL, className=NULL, debounce=NULL, disabled=NULL, forwardText=NULL, isLastPage=NULL, itemRangeText=NULL, itemText=NULL, itemsPerPageText=NULL, loading_state=NULL, n_blur=NULL, n_submit=NULL, onChange=NULL, page=NULL, pageInputDisabled=NULL, pageNumberText=NULL, pageRangeText=NULL, pageSelectLabelText=NULL, pageSize=NULL, pageSizeInputDisabled=NULL, pageSizes=NULL, pageText=NULL, pagesUnknown=NULL, persisted_props=NULL, persistence=NULL, persistence_type=NULL, size=NULL, style=NULL, text=NULL, totalItems=NULL, value=NULL) {
    
    props <- list(children=children, id=id, backwardText=backwardText, className=className, debounce=debounce, disabled=disabled, forwardText=forwardText, isLastPage=isLastPage, itemRangeText=itemRangeText, itemText=itemText, itemsPerPageText=itemsPerPageText, loading_state=loading_state, n_blur=n_blur, n_submit=n_submit, onChange=onChange, page=page, pageInputDisabled=pageInputDisabled, pageNumberText=pageNumberText, pageRangeText=pageRangeText, pageSelectLabelText=pageSelectLabelText, pageSize=pageSize, pageSizeInputDisabled=pageSizeInputDisabled, pageSizes=pageSizes, pageText=pageText, pagesUnknown=pagesUnknown, persisted_props=persisted_props, persistence=persistence, persistence_type=persistence_type, size=size, style=style, text=text, totalItems=totalItems, value=value)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'Pagination',
        namespace = 'carbon_dash',
        propNames = c('children', 'id', 'backwardText', 'className', 'debounce', 'disabled', 'forwardText', 'isLastPage', 'itemRangeText', 'itemText', 'itemsPerPageText', 'loading_state', 'n_blur', 'n_submit', 'onChange', 'page', 'pageInputDisabled', 'pageNumberText', 'pageRangeText', 'pageSelectLabelText', 'pageSize', 'pageSizeInputDisabled', 'pageSizes', 'pageText', 'pagesUnknown', 'persisted_props', 'persistence', 'persistence_type', 'size', 'style', 'text', 'totalItems', 'value'),
        package = 'carbonDash'
        )

    structure(component, class = c('dash_component', 'list'))
}
