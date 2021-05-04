library(shiny) 
dl<-read.table("https://health.data.ny.gov/resource/xdss-u53e.csv?$limit=50000", header=TRUE, sep=",")
# Define UI for app that draws a histogram ----
ui <- fluidPage(
  
  # App title ----
  titlePanel("My Covid App"),
  
  # Sidebar layout with input and output definitions ----
  sidebarLayout(
    
    # Sidebar panel for inputs ----
    sidebarPanel(
      
      radioButtons(
      inputId="daily",
      label="Do you want to see cumulative or daily counts?",
      choices = c("daily","cumulative"),
      selected = NULL,
      inline = TRUE,
      width = NULL,
      choiceNames = NULL,
      choiceValues = NULL),
      
      radioButtons(
        inputId="country",
        label="Select your county",
        choices = unique(dl$county),
        selected = NULL,
        inline = TRUE,
        width = NULL,
        choiceNames = NULL,
        choiceValues = NULL
      )
    ),
    
    # Main panel for displaying outputs ----
    mainPanel(
      
      # Output: Histogram ----
      plotOutput(outputId = "distPlot")
      
    )
  )
)
# Define server logic required to draw a histogram ----
server <- function(input, output) {
  
  # Histogram of the Old Faithful Geyser Data ----
  # with requested number of bins
  # This expression that generates a histogram is wrapped in a call
  # to renderPlot to indicate that:
  #
  # 1. It is "reactive" and therefore should be automatically
  #    re-executed when inputs (input$bins) change
  # 2. Its output type is a plot
  output$distPlot <- renderPlot({
    sb<-subset(dl, dl$county==input$ county)  
    
    if (input$daily=="cumulative"){
      plot(sb$cumulative_number_of_positives,type = "p",col = "red", xlab = "Month", ylab = "Cumulative cases", 
           main = "COVID cases")
    }
    else{
      
      plot(sb$new_positives,type = "p",col = "red", xlab = "Month", ylab = "Daily cases", 
           main = "COVID cases")
    }
    
  })
  
}
shinyApp(ui = ui, server = server)