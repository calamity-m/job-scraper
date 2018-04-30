import React from 'react'
import Link from 'gatsby-link'
import ReactTable from "react-table";
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

    state = {
        date: []
    }

    render() {

        var jsonData = '{"message": [{"title": "ACT opportunities for Australian Citizens Only", "company": "Powerstaff Consulting", "location": "Canberra ACT", "description": "Windows Server Engineer.Software & Middleware Developer.Below is a list of contract positions we have been recruiting for the ACT....", "date": "Just posted", "salary": "Not Specified", "link": "https://au.indeed.com/rc/clk?jk=00e1ef7b1639ab60&fccid=82a7a85a33bbba3b&vjs=3"}, {"title": "Tools & Automation Engineer", "company": "Leidos", "location": "Canberra ACT", "description": "Supporting the catalogue service offering for the Centralised Processing Program, you will be primarily responsible for providing support to Service Catalogue...", "date": "Today", "salary": "Not Specified", "link": "https://au.indeed.com/rc/clk?jk=235ec1dc4a0e0508&fccid=8765a4045377753a&vjs=3"}, {"title": "Security Architect/Software Support Engineers", "company": "Whizdom Recruitment", "location": "Canberra ACT", "description": "Role description This position has responsibility for leading design activities and implementation oversight in alignment with ASD architectural guidance...", "date": "Today", "salary": "Not Specified", "link": "https://au.indeed.com/rc/clk?jk=a038daf8cf1ec791&fccid=7a0dce90dae6e736&vjs=3"}, {"title": "System Integration Engineer - Oracle", "company": "Talent International", "location": "Canberra ACT", "description": "A proven track record in administering Oracle Fusion Middleware (OFM) software. Close collaboration with Software Development and QA teams with a DevOps mindset...", "date": "3 days ago", "salary": "Not Specified", "link": "https://au.indeed.com/rc/clk?jk=86142105b1d90dc7&fccid=ea1f64b071408cc5&vjs=3"}, {"title": "Java Developer", "company": "Paxus", "location": "Canberra ACT", "description": "Current opportunity for an NV1 Cleared Java Developer with Oracle Identity Management experience The Java Developer would need to have NV1 (Minimum) and the...", "date": "3 days ago", "salary": "Not Specified", "link": "https://au.indeed.com/rc/clk?jk=dd71c0baf2287a41&fccid=0be9b830285b4790&vjs=3"}, {"title": "DevOps Engineer", "company": "Talent International", "location": "Canberra ACT", "description": "Good fundamental computer science / software engineering skills and knowledge, particularly operating system internals, memory management, and networking....", "date": "3 days ago", "salary": "$90,000 - $100,000 a year", "link": "https://au.indeed.com/rc/clk?jk=d100f967122dc0b4&fccid=ea1f64b071408cc5&vjs=3"}, {"title": "Land Hydrographer/Surveyor Traineeship", "company": "Trans-Civ", "location": "Canberra ACT", "description": "Undertake data analysis using both proprietary and supplier based computer software packages. This job is ideally suited to combat soldiers (Artillery surveying...", "date": "3 days ago", "salary": "Not Specified", "link": "https://au.indeed.com/rc/clk?jk=4101b51548407610&fccid=c780468ff75ef5b3&vjs=3"}, {"title": "Red Hat Enterprise Linux Consultant | Canberra | Any AGSVA Clearance", "company": "Vertical Scope Defence Industry Recruitment", "location": "Canberra ACT", "description": "Red Hat Certified Engineer (RHCE) certification; This multinational software company provides a range of consultative services like storage, operating systems...", "date": "3 days ago", "salary": "$145,000 - $150,000 a year", "link": "https://au.indeed.com/company/Vertical-Scope-Defence-Industry-Recruitment/jobs/Red-Hat-Enterprise-Linux-Consultant-Agsva-Clearance-96db463f65041235?fccid=ca83a8dfc8725d1a&vjs=3"}, {"title": "Systems Engineer - Australia", "company": "DRS Technologies", "location": "Canberra ACT", "description": "Perform network troubleshooting and internet third party product interfaces, hardware, software and firmware. The Senior Systems Integration Engineer reports to...", "date": "4 days ago", "salary": "Not Specified", "link": "https://au.indeed.com/rc/clk?jk=26d1d22c1ebfe848&fccid=47f7fd9a91f2805c&vjs=3"}, {"title": "Java Developer Canberra, Australia", "company": "Salt Recruitment", "location": "Canberra ACT", "description": "Canberra Global Digital Consultancy 6-month Contract (Daily Rates) Technology, Agency / Temp, Canberra AU$1000 - AU$1200.00 per day The client Salt have...", "date": "4 days ago", "salary": "$1,000 - $1,200 a day", "link": "https://au.indeed.com/rc/clk?jk=1e3b78de22390ec6&fccid=d35f6b081e467c24&vjs=3"}]}';
        var jsonObj = JSON.parse(jsonData)

        const jobData = jsonObj.message;

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
