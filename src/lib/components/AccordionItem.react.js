import React, { Component } from 'react';
import PropTypes from 'prop-types';
import * as LazyLoader from '../LazyLoader';

/**
 * AccordionItem is a wrapper for the Carbon AccordionItem component.
 */
export default class AccordionItem extends Component {
    render() {
        const {
            className,
            ...otherProps
        } = this.props;
        const { title } = this.props;
        const { open } = this.props;

        const RealComponent = LazyLoader['AccordionItem'];
        if (!RealComponent) {
            return null;
        }

        return (
            <React.Suspense fallback={null}>
                <RealComponent 
                    className={className}
                    title={title}
                    open={open}
                    {...otherProps}
                />
            </React.Suspense>
        );
    }
}

AccordionItem.defaultProps = {
    className: '',
    title: 'Accordion Title',
    open: false,
};

AccordionItem.propTypes = {
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

    /**
     * disabled
     */
    disabled: PropTypes.any,

    /**
     * onClick
     */
    onClick: PropTypes.any,

    /**
     * onHeadingClick
     */
    onHeadingClick: PropTypes.any,

    /**
     * open
     */
    open: PropTypes.bool,

    /**
     * renderExpando
     */
    renderExpando: PropTypes.any,

    /**
     * renderToggle
     */
    renderToggle: PropTypes.any,

    /**
     * title
     */
    title: PropTypes.node,

};
