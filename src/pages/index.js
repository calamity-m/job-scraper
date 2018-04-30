import React from 'react'
import Link from 'gatsby-link'
import ReactTable from "react-table";
import axios from "axios";
import 'react-table/react-table.css'


const IndexPage = () => (
  <div>
    <h1>Hi people</h1>
    <p>Welcome to your new Gatsby site.</p>
    <p>Now go build something great.</p>
    <Link to="/page-2/">Go to page 2</Link>
  </div>
)

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
                accessor: 'location' // String-based value accessors!
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
            }]

        return (
            <div>
                <h1>HELLO M8S!</h1>
                <p>Welcome to your new Gatsby site.</p>
                <p>Now go build something great.</p>
                <Link to="/page-2/">Go to page 2</Link>
                <p>{jsonObj.message[0].title}</p>
                <ReactTable
                    data={jobData}
                    columns={jobColumns}
                    defaultPageSize={10}
                />
            </div>    

            
        )
    }

}

export default IndexPageC
