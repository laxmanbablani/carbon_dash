import React, { Component } from 'react';
import PropTypes from 'prop-types';
import * as LazyLoader from '../LazyLoader';

/**
 * Pagination is a wrapper for the Carbon Pagination component.
 */
export default class Pagination extends Component {
    render() {
        const {
            className,
            ...otherProps
        } = this.props;
        const { value } = this.props;

        const RealComponent = LazyLoader['Pagination'];
        if (!RealComponent) {
            return null;
        }

        return (
            <React.Suspense fallback={null}>
                <RealComponent 
                    className={className}
                    value={value}
                    {...otherProps}
                />
            </React.Suspense>
        );
    }
}

Pagination.defaultProps = {
    className: '',
    value: '',
};

Pagination.propTypes = {
    /** id */
    id: PropTypes.string,

    /** children */
    children: PropTypes.node,

    /** className */
    className: PropTypes.string,

    /** style */
    style: PropTypes.object,

    /** setProps */
    setProps: PropTypes.func,

    /** loading_state */
    loading_state: PropTypes.shape({ is_loading: PropTypes.bool, prop_name: PropTypes.string, component_name: PropTypes.string }),

    /** persistence */
    persistence: PropTypes.oneOfType([PropTypes.bool, PropTypes.string, PropTypes.number]),

    /** persisted_props */
    persisted_props: PropTypes.arrayOf(PropTypes.string),

    /** persistence_type */
    persistence_type: PropTypes.oneOf(['local', 'session', 'memory']),

    /** n_blur */
    n_blur: PropTypes.number,

    /** n_submit */
    n_submit: PropTypes.number,

    /** debounce */
    debounce: PropTypes.oneOfType([PropTypes.bool, PropTypes.number]),

    /**
     * backwardText
     */
    backwardText: PropTypes.any,

    /**
     * disabled
     */
    disabled: PropTypes.any,

    /**
     * forwardText
     */
    forwardText: PropTypes.any,

    /**
     * isLastPage
     */
    isLastPage: PropTypes.any,

    /**
     * itemRangeText
     */
    itemRangeText: PropTypes.any,

    /**
     * itemText
     */
    itemText: PropTypes.any,

    /**
     * itemsPerPageText
     */
    itemsPerPageText: PropTypes.any,

    /**
     * onChange
     */
    onChange: PropTypes.any,

    /**
     * page
     */
    page: PropTypes.any,

    /**
     * pageInputDisabled
     */
    pageInputDisabled: PropTypes.any,

    /**
     * pageNumberText
     */
    pageNumberText: PropTypes.any,

    /**
     * pageRangeText
     */
    pageRangeText: PropTypes.any,

    /**
     * pageSelectLabelText
     */
    pageSelectLabelText: PropTypes.any,

    /**
     * pageSize
     */
    pageSize: PropTypes.any,

    /**
     * pageSizeInputDisabled
     */
    pageSizeInputDisabled: PropTypes.any,

    /**
     * pageSizes
     */
    pageSizes: PropTypes.any,

    /**
     * text
     */
    text: PropTypes.any,

    /**
     * value
     */
    value: PropTypes.any,

    /**
     * pageText
     */
    pageText: PropTypes.any,

    /**
     * pagesUnknown
     */
    pagesUnknown: PropTypes.any,

    /**
     * size
     */
    size: PropTypes.any,

    /**
     * totalItems
     */
    totalItems: PropTypes.any,

};
