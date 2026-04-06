import React, { Component } from 'react';
import PropTypes from 'prop-types';
import * as LazyLoader from '../LazyLoader';

/**
 * TabsVertical is a wrapper for the Carbon TabsVertical component.
 */
export default class TabsVertical extends Component {
    render() {
        const {
            className,
            ...otherProps
        } = this.props;
        const { selectedIndex } = this.props;

        const RealComponent = LazyLoader['TabsVertical'];
        if (!RealComponent) {
            return null;
        }

        return (
            <React.Suspense fallback={null}>
                <RealComponent 
                    className={className}
                    selectedIndex={selectedIndex}
                    {...otherProps}
                />
            </React.Suspense>
        );
    }
}

TabsVertical.defaultProps = {
    className: '',
    selectedIndex: -1,
};

TabsVertical.propTypes = {
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
     * defaultSelectedIndex
     */
    defaultSelectedIndex: PropTypes.any,

    /**
     * height
     */
    height: PropTypes.any,

    /**
     * onChange
     */
    onChange: PropTypes.any,

    /**
     * selectedIndex
     */
    selectedIndex: PropTypes.number,

};
