import React, { Component } from 'react';
import PropTypes from 'prop-types';
import * as LazyLoader from '../LazyLoader';

/**
 * SideNavFooter is a wrapper for the Carbon SideNavFooter component.
 */
export default class SideNavFooter extends Component {
    render() {
        const {
            className,
            ...otherProps
        } = this.props;
        const { expanded } = this.props;

        const RealComponent = LazyLoader['SideNavFooter'];
        if (!RealComponent) {
            return null;
        }

        return (
            <React.Suspense fallback={null}>
                <RealComponent 
                    className={className}
                    expanded={expanded}
                    {...otherProps}
                />
            </React.Suspense>
        );
    }
}

SideNavFooter.defaultProps = {
    className: '',
    expanded: false,
};

SideNavFooter.propTypes = {
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

    /**
     * assistiveText
     */
    assistiveText: PropTypes.any,

    /**
     * expanded
     */
    expanded: PropTypes.bool,

    /**
     * onToggle
     */
    onToggle: PropTypes.any,

};
