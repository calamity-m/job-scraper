import React from 'react'
import Link from 'gatsby-link'
import ReactTable from "react-table";
import axios from "axios";
import 'react-table/react-table.css';

class IndexPageC extends React.Component {

    constructor(props) {
        super(props)

        this.state = {
            apiData: []
        }
    }

    componentDidMount() {
        
        axios.get('https://wbnd78ok7l.execute-api.us-west-2.amazonaws.com/dev/ping')
            .then(response => {
                this.setState({
                    apiData: response.data.message
                })
            })
            .catch(err => console.log(err))
        
    }

    render() {
        
        const jobData = this.state.apiData;

        const jobColumns = [{
                Header: 'Location',
                accessor: 'location',
                width: 75
            }, {
                Header: 'Title',
                accessor: 'title',
            }, {
                Header: 'Company',
                accessor: 'company',
            }, {
                Header: 'Summary',
                accessor: 'description',
            }, {
                Header: 'Salary',
                accessor: 'salary',
            }, {
                Header: 'Date',
                accessor: 'date',
                width: 100
            }, {
                Header: 'Link',
                accessor: 'link',
            }]

        return (
            <div>
                <h1>Main Listed Jobs</h1>
                <p>Below is a table of freshly web-scraped jobs.</p>
                <ReactTable
                    data={jobData}
                    columns={jobColumns}
                    defaultPageSize={10}
                />
                <p>NOTE: Jobs scraped from au.indeed.com </p>
                <br />
                <p> Copyright Mark Monteno (u3154816) </p>
            </div>    

            
        )
    }

}

export default IndexPageC
