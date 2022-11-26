namespace Temperature_App
{
    partial class Form1
    {
        /// <summary>
        ///  Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        ///  Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        ///  Required method for Designer support - do not modify
        ///  the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            this.Convbtn = new System.Windows.Forms.Button();
            this.Celsiuslst = new System.Windows.Forms.ListBox();
            this.Fahrenheitlst = new System.Windows.Forms.ListBox();
            this.SuspendLayout();
            // 
            // Convbtn
            // 
            this.Convbtn.Location = new System.Drawing.Point(348, 349);
            this.Convbtn.Name = "Convbtn";
            this.Convbtn.Size = new System.Drawing.Size(75, 23);
            this.Convbtn.TabIndex = 0;
            this.Convbtn.Text = "Convert";
            this.Convbtn.UseVisualStyleBackColor = true;
            this.Convbtn.Click += new System.EventHandler(this.Convbtn_Click);
            // 
            // Celsiuslst
            // 
            this.Celsiuslst.FormattingEnabled = true;
            this.Celsiuslst.ItemHeight = 15;
            this.Celsiuslst.Location = new System.Drawing.Point(48, 23);
            this.Celsiuslst.Name = "Celsiuslst";
            this.Celsiuslst.Size = new System.Drawing.Size(237, 349);
            this.Celsiuslst.TabIndex = 4;
            // 
            // Fahrenheitlst
            // 
            this.Fahrenheitlst.FormattingEnabled = true;
            this.Fahrenheitlst.ItemHeight = 15;
            this.Fahrenheitlst.Location = new System.Drawing.Point(477, 23);
            this.Fahrenheitlst.Name = "Fahrenheitlst";
            this.Fahrenheitlst.Size = new System.Drawing.Size(236, 349);
            this.Fahrenheitlst.TabIndex = 5;
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(7F, 15F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(800, 450);
            this.Controls.Add(this.Fahrenheitlst);
            this.Controls.Add(this.Celsiuslst);
            this.Controls.Add(this.Convbtn);
            this.Name = "Form1";
            this.Text = "Form1";
            this.ResumeLayout(false);

        }

        #endregion
        private Button Convbtn;
        private ListBox Celsiuslst;
        private ListBox Fahrenheitlst;
    }
}