cmake_minimum_required(VERSION 3.15)
project(jsidl_xml LANGUAGES NONE)

install(
    DIRECTORY urn.jaus.jss.core-v1.1 urn.jaus.jss.environment_sensing urn.jaus.jss.manipulator urn.jaus.jss.mobility urn.jaus.jss.ugv
    DESTINATION res
    FILES_MATCHING
    PATTERN "urn*.xml"
)
