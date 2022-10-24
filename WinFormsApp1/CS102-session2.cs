using Microsoft.VisualBasic;


namespace CS102session2
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            //InitializeComponent();

            this.Close();
            var gradestr = Interaction.InputBox("Student's grade", "Grading Portal", "");
            try
            {
                int grade = (int)Convert.ToInt64(gradestr);

                switch (grade)
                {
                    case >= 90:
                        MessageBox.Show("A");
                        break;

                    case >= 80:
                        MessageBox.Show("B");
                        break;

                    case >= 70:
                        MessageBox.Show("C");
                        break;

                    case >= 60:
                        MessageBox.Show("D");
                        break;

                    case < 60:
                        MessageBox.Show("F");
                        break;



                }
            }
            catch (System.FormatException)
            {
                MessageBox.Show("Invalid Format");
            }

            
                    //this.Close();



            }
    }
}